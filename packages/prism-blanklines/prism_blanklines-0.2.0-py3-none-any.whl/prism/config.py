"""
Configuration management for prism blank line rules.
Copyright (c) 2025-2026 Greg Smethells. All rights reserved.
See the accompanying AUTHORS file for a complete list of authors.
This file is subject to the terms and conditions defined in LICENSE.
"""

import tomllib
from .types import BlockType
from dataclasses import dataclass, field

@dataclass
class BlankLineConfig:
  """Configuration for blank line rules between block types"""
  defaultBetweenDifferent: int = 1
  transitions: dict = field(default_factory=dict)
  consecutiveControl: int = 1
  consecutiveDefinition: int = 1
  indentWidth: int = 2

  @classmethod
  def fromToml(cls, configPath):
    """Load configuration from TOML file
    :param configPath: Path to prism.toml file
    :type configPath: Path
    :rtype: BlankLineConfig
    :raises: ValueError for invalid configuration values
    :raises: FileNotFoundError if config file doesn't exist
    """
    if not configPath.exists():
      raise FileNotFoundError(f'Configuration file not found: {configPath}')

    try:
      with open(configPath, 'rb') as f:
        data = tomllib.load(f)
    except tomllib.TOMLDecodeError as e:
      raise ValueError(f'Failed to parse TOML file {configPath}: {e}')
    except OSError as e:
      raise ValueError(f'Failed to read TOML file {configPath}: {e}')

    blankLinesConfig = data.get('blank_lines', {})

    # Parse default value
    defaultBetweenDifferent = blankLinesConfig.get('default_between_different', 1)

    cls._validateBlankLineCount(defaultBetweenDifferent, 'default_between_different')

    # Parse special rules
    consecutiveControl = blankLinesConfig.get('consecutive_control', 1)
    consecutiveDefinition = blankLinesConfig.get('consecutive_definition', 1)

    cls._validateBlankLineCount(consecutiveControl, 'consecutive_control')
    cls._validateBlankLineCount(consecutiveDefinition, 'consecutive_definition')

    # Parse indent width
    indentWidth = blankLinesConfig.get('indent_width', 2)
    cls._validateBlankLineCount(indentWidth, 'indent_width')

    # Parse transition overrides
    transitions = {}

    for key, value in blankLinesConfig.items():
      if key in ['default_between_different', 'consecutive_control', 'consecutive_definition', 'indent_width']:
        continue

      # Parse transition key (e.g., "assignment_to_call")
      parts = key.split('_to_')

      if len(parts) != 2:
        raise ValueError(f'Invalid transition key format: {key}. Expected format: blocktype_to_blocktype')

      fromBlockName, toBlockName = parts

      try:
        fromBlock = cls._parseBlockType(fromBlockName)
        toBlock = cls._parseBlockType(toBlockName)
      except ValueError as e:
        raise ValueError(f'Invalid transition key {key}: {e}')

      cls._validateBlankLineCount(value, key)
      transitions[(fromBlock, toBlock)] = value

    return cls(
      defaultBetweenDifferent=defaultBetweenDifferent,
      transitions=transitions,
      consecutiveControl=consecutiveControl,
      consecutiveDefinition=consecutiveDefinition,
      indentWidth=indentWidth,
    )

  @classmethod
  def fromDefaults(cls) -> 'BlankLineConfig':
    """Create configuration with default values (current behavior)
    :rtype: BlankLineConfig
    """
    return cls()

  def getBlankLines(self, fromBlock, toBlock):
    """Get number of blank lines for transition between block types
    :param fromBlock: Source block type
    :type fromBlock: BlockType
    :param toBlock: Target block type
    :type toBlock: BlockType
    :rtype: int
    """
    # Check for specific transition override first
    key = (fromBlock, toBlock)

    if key in self.transitions:
      blankLines = self.transitions[key]
    elif fromBlock == toBlock:
      # Handle same-type special rules
      if fromBlock == BlockType.CONTROL:
        blankLines = self.consecutiveControl
      elif fromBlock == BlockType.DEFINITION:
        blankLines = self.consecutiveDefinition
      else:
        # Same type blocks (except Control/Definition) have no blank lines
        blankLines = 0
    else:
      # Use default for different block types
      blankLines = self.defaultBetweenDifferent

    return blankLines

  @staticmethod
  def _parseBlockType(blockTypeName: str) -> BlockType:
    """Parse block type name from string
    :param blockTypeName: Name of block type (e.g., 'assignment', 'call')
    :type blockTypeName: str
    :rtype: BlockType
    :raises: ValueError if block type name is invalid
    """
    blockTypeMap = {
      'assignment': BlockType.ASSIGNMENT,
      'call': BlockType.CALL,
      'import': BlockType.IMPORT,
      'control': BlockType.CONTROL,
      'definition': BlockType.DEFINITION,
      'declaration': BlockType.DECLARATION,
      'comment': BlockType.COMMENT,
    }

    if blockTypeName not in blockTypeMap:
      validNames = ', '.join(blockTypeMap.keys())

      raise ValueError(f'Unknown block type: {blockTypeName}. Valid types: {validNames}')

    return blockTypeMap[blockTypeName]

  @staticmethod
  def _validateBlankLineCount(value: int, key: str):
    """Validate blank line count is in valid range (0-3)
    :param value: Blank line count to validate
    :type value: int
    :param key: Configuration key name for error messages
    :type key: str
    :raises: ValueError if value is invalid
    """
    if not isinstance(value, int):
      raise ValueError(f'{key} must be an integer, got {type(value).__name__}: {value}')

    if value < 0 or value > 3:
      raise ValueError(f'{key} must be between 0 and 3, got: {value}')

# Global configuration instance available for import
config = BlankLineConfig.fromDefaults()

def setConfig(newConfig):
  """Update the global configuration instance
  :param newConfig: Configuration to set as global
  :type newConfig: BlankLineConfig
  """
  global config

  config = newConfig
