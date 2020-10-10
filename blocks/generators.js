Blockly.Python['dht12_read'] = function(block) {
  Blockly.Python.definitions_['import_DHT12'] = 'import DHT12';

  var dropdown_valueindex = block.getFieldValue('valueIndex');
  var code = `DHT12.read()[${dropdown_valueindex}]`;
  return [code, Blockly.Python.ORDER_NONE];
};
