Blockly.defineBlocksWithJsonArray([
{
  "type": "dht12_read",
  "message0": "DHT12 read %1",
  "args0": [
    {
      "type": "field_dropdown",
      "name": "valueIndex",
      "options": [
        [
          "temperature (°C)",
          "0"
        ],
        [
          "humidity (%RH)",
          "1"
        ]
      ]
    }
  ],
  "inputsInline": true,
  "output": "Number",
  "colour": "#3498DB",
  "tooltip": "",
  "helpUrl": ""
}
]);
