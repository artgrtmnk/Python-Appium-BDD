Feature: Manual weight change

  Background:
    Given the app is launched

  Scenario Outline: changing weight using record screen
    When tap on plus sign in the top right corner
    Then record screen is opened
    When tap on Weight
    Then add weight screen is opened
    When enter "<weight>" in the weight field
    And enter "<fat mass>" in the fat mass field
    And tap save button
    Then home screen is opened
    And weight is "<weight>"
    And fat mass is "<fat mass>"
    Examples:
    | weight | fat mass |
    | 70     | 5        |
    | 65.5   | 3        |
    | 75     | 7.1      |
    | 60.2   | 2.1      |