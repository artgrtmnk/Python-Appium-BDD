Feature: Manual weight change

  Background:
    Given user launched the app

  Scenario Outline: changing weight using record screen
    When user tap on plus sign in the top right corner
    Then record screen is opened
    When user tap on Weight
    Then add weight screen is opened
    When user enter "<weight>" in the weight field
    And user enter "<fat mass>" in the fat mass field
    And user tap save button
    Then home screen is opened
    And weight is "<weight>"
    And fat mass is "<fat mass>"
    Examples:
    | weight | fat mass |
    | 70     | 5        |
    | 65.5   | 7.1      |
    | 1      | 0.1     |
    | 599.9  | 599    |