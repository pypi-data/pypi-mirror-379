from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _

from netbox_firmware.models import *
from netbox_firmware.choices import *
from netbox.choices import *
from netbox.forms import NetBoxModelImportForm
from utilities.forms.fields import (
    CSVChoiceField, CSVContentTypeField, CSVModelChoiceField, CSVModelMultipleChoiceField, CSVTypedChoiceField,
    SlugField,
)

### Firmware ###


class FirmwareImportForm(NetBoxModelImportForm):
    name = forms.CharField(
        label=_('Name'),
        required=True,
        help_text=_('Name of the firmware')
    )
    manufacturer = CSVModelChoiceField(
        label=_('Manufacturer'),
        queryset=Manufacturer.objects.all(),
        to_field_name='name',
        required=True,
        help_text=_('Firmware type manufacturer')
    )
    file_name = forms.CharField(
        label=_('File name'),
        required=False,
        help_text=_('File name of the firmware')
    )
    device_type = CSVModelMultipleChoiceField(
        label=_('Device Type name'),
        queryset=DeviceType.objects.all(),
        to_field_name='model',
        required=False,
        help_text=_('Name of the Device Type. / List if the Firmware supports multiple Device Type')
    )
    module_type = CSVModelMultipleChoiceField(
        label=_('Module Type name'),
        queryset=ModuleType.objects.all(),
        to_field_name='model',
        required=False,
        help_text=_('Name of the Module Type. / List if the Firmware supports multiple Module Type')
    )
    status = CSVChoiceField(
        label=_('Status'),
        choices=FirmwareStatusChoices,
        required=False,
        help_text=_('Operational status. / Default = Active')
    )
    description = forms.CharField(
        label=_('Description'),
        required=False,
        help_text=_('Description of the firmware')
    )
    comments = forms.CharField(
        label=_('Comments'),
        required=False,
        help_text=_('Additional comments about the firmware')
    )

    class Meta:
        model = Firmware
        fields = [
            'name', 
            'manufacturer',
            'file_name', 
            'status', 
            'description', 
            'device_type',
            'module_type',
            'comments',
            ]


    ### Check if only 1 type field is used.
    def clean(self):
        super().clean()
        device_type = self.cleaned_data.get('device_type')
        module_type = self.cleaned_data.get('module_type')

        # Ensure only one of device_type or module_type is set, not both
        if device_type and module_type:
            raise forms.ValidationError(
                "You cannot specify both Device Type and Module Type for a single firmware entry."
            )

    ### This will validate that all listed DeviceType belong to the selected Manufacturer.
    def clean_device_type(self):
        device_type_list = self.cleaned_data.get('device_type')
        manufacturer = self.cleaned_data.get('manufacturer')

        # 1st condition : If list is empty = No validation needed.
        if not device_type_list:
            return device_type_list

        # 2th condition : Check if all device_types belong to the selected manufacturer.
        if device_type_list and manufacturer:
            mismatched = [
                dt for dt in device_type_list if dt.manufacturer != manufacturer
            ]
            if mismatched:
                mismatched_names = ", ".join(str(dt) for dt in mismatched)
                raise forms.ValidationError(
                    f"The following DeviceTypes do not belong to the selected manufacturer '{manufacturer}': {mismatched_names}"
                )

        return device_type_list

   

    ### This will validate that all listed ModuleType belong to the selected Manufacturer.
    def clean_module_type(self):
        module_type_list = self.cleaned_data.get('module_type')
        manufacturer = self.cleaned_data.get('manufacturer')

        # 1st condition : If list is empty = No validation needed.
        if not module_type_list:
            return module_type_list 

        # 2th condition : Check if all module_types belong to the selected manufacturer.
        if module_type_list and manufacturer:
            mismatched = [
                mt for mt in module_type_list if mt.manufacturer != manufacturer
            ]
            if mismatched:
                mismatched_names = ", ".join([str(mt) for mt in mismatched])
                raise forms.ValidationError(
                    f"The following ModuleTypes do not belong to the selected manufacturer '{manufacturer}': {mismatched_names}"
                )

        return module_type_list


### FirmwareAssignment ###


class FirmwareAssignmentImportForm(NetBoxModelImportForm):
    firmware = CSVModelChoiceField(
        label=_('Firmware'),
        queryset=Firmware.objects.all(),
        to_field_name='name',
        help_text=_('Firmware name')
    )
    manufacturer = CSVModelChoiceField(
        label=_('Manufacturer'),
        queryset=Manufacturer.objects.all(),
        to_field_name='name',
        help_text=_('Device type manufacturer')
    )
    hardware_kind = CSVTypedChoiceField(
        label=_('Hardware kind'),
        choices=HardwareKindChoices,
        required=True,
        help_text=_('Type of hardware')
    )
    hardware_name = forms.CharField(
        label=_('Hardware name'),
        required=True,
        help_text=_('Name of the hardware, e.g. device name or module id/serial')
    )
    comments = forms.CharField(
        label=_('Comments'),
        required=False,
        help_text=_('Additional comments about the firmware assignment')
    )
    patch_date = forms.DateField(
        label=_('Patch date'),
        required=False,
        help_text=_('Date of the firmware patch')
    )
    ticket_number = forms.CharField(
        label=_('Ticket number'),
        required=False,
        help_text=_('Ticket number of the firmware patch')
    )
    description = forms.CharField(
        label=_('Description'),
        required=False,
        help_text=_('Description of the firmware assignment')
    )

    class Meta:
        model = FirmwareAssignment
        fields = [
            'firmware', 
            'manufacturer', 
            'hardware_kind', 
            'hardware_name', 
            'patch_date', 
            'ticket_number', 
            'description',
            'comments',
            ]

    def clean(self):
        super().clean()
        pass
    
    def _clean_fields(self):
        return super()._clean_fields()

    def _get_validation_exclusions(self):
        exclude = super()._get_validation_exclusions()
        exclude.remove('device')
        exclude.remove('module')
        return exclude

    def clean_hardware_name(self):
        hardware_kind = self.cleaned_data.get('hardware_kind')
        manufacturer = self.cleaned_data.get('manufacturer')
        model = self.cleaned_data.get('hardware_name')

        if not hardware_kind or not manufacturer:
            return None

        try:
            if hardware_kind == 'device':
                hardware_type = Device.objects.get(
                    device_type__manufacturer=manufacturer, name=model
                )
                existing = FirmwareAssignment.objects.filter(device__name=model).first()
                if existing and existing.id != self.instance.id:
                    raise ValidationError(f'Device "{model}" already has a Firmware assigned.')

            elif hardware_kind == 'module':
                if model.isdigit():
                    hardware_type = Module.objects.get(
                        module_type__manufacturer=manufacturer, pk=model
                    )
                    existing = FirmwareAssignment.objects.filter(module__pk=model).first()
                else:
                    hardware_type = Module.objects.get(
                        module_type__manufacturer=manufacturer, serial=model
                    )
                    existing = FirmwareAssignment.objects.filter(module__serial=model).first()

                if existing and existing.id != self.instance.id:
                    raise ValidationError(f'Module "{model}" already has a Firmware assigned.')

        except ObjectDoesNotExist:
            raise forms.ValidationError(
                f'Hardware type not found: "{hardware_kind}", "{manufacturer}", "{model}"'
            )

        setattr(self.instance, f'{hardware_kind}', hardware_type)
        return hardware_type

    def _get_clean_value(self, field_name):
        try:
            return self.base_fields[field_name].clean(self.data.get(field_name))
        except forms.ValidationError as e:
            self.add_error(field_name, e)
            raise