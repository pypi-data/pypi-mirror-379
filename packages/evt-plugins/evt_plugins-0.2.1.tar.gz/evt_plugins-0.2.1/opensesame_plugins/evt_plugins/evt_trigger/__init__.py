"""A plugin for generating triggers with EVT devices."""

# The category determines the group for the plugin in the item toolbar
category = "RUG/BSS hardware"
# Defines the GUI controls:
controls = [
    {
        "type": "combobox",
        "var": "device",
        "label": "Select device :",
        "options": [
            "DUMMY"
        ],
        "name": "device_combobox_widget",
        "tooltip": "Select the desired EVT-device or DUMMY."
    }, {
        "type": "checkbox",
        "var": "refresh",
        "label": "Refresh device list",
        "name": "refresh_checkbox_widget",
        "tooltip": "Refresch device list checkbox"
    }, {
        "type": "combobox",
        "var": "outputmode",
        "label": "Select output mode :",
        "options": [
            "Clear output lines",
            "Write output lines",
            "Invert output lines",
            "Pulse output lines"
        ],
        "name": "output_mode_combobox_widget",
        "tooltip": "Select the desired output mode"
     }, {
        "type": "line_edit",
        "var": "mask",
        "label": "Byte or bit-mask value :",
        "name": "byte_value_line_edit_widget",
        "tooltip": "Bit mask value [0-255]"
    }, {
        "type": "line_edit",
        "var": "duration",
        "label": "Duration [ms] :",
        "name": "duration_line_edit_widget",
        "tooltip": "Expecting a value in milliseconds"
    }, {
        "type": "checkbox",
        "var": "close_device",
        "label": "Auto close EVT-device(s). (Use this for the latter instance of the plugin or with a single instance of the plugin.)",
        "name": "close_device_checkbox_widget",
        "tooltip": "Close device list checkbox"
    }, {
        "type": "text",
        "label": "<small>EVT-trigger plug-in version 0.2.1</small>"
    }
]
