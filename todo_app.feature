Feature: TODO Task handling
    Scenario: Show the welcome text on the screen
    When the feature is started
    Then result is
    """
    Command Line Todo application
    =============================
    How to Use :
    Command line arguments:
        -l   Lists all the tasks
        -a   Adds a new task
        -r   Removes an task
        -c   Completes an task
    """


    Scenario: List all the task when do not have any task
        When arguments is "-l'
        Then the value on the screen is "No todos for today! :)"

    Scenario: List all the task when we have only 1 task
        Given the first task is "Walk the dog"
        When the argument is "-l"

    Scenario: List all the task when you have more than one task
        Given the first task ds "Walk the dog" and the second task is "Buy Milk"
        When the argument is "-l'
        Then the result is
        """
        1 - Walk the dog
        2 - Buy milk
        """
    Scenario: Adding a new task to the application
        Given the first task is "Walk the dog" and the second task is "Buy mile
        When the argument is "-a" and the value is "Feed the monkey'
         Then the result is
    """
    1 - Walk the dog
    2 - Buy milk
    3 - Feed the monkey
    """

    Scenario: Add new task error handling
        Given the terminal is opened in the project
        When the application is run with the '-a' argument
        Then it should show an error message like "Unable to add: No task provided"

    Scenario: Remove one task
        Given the task is 'Walk the dog'
        When the application is run with '-r' argument
        Then it should remove "Walk the dog" form the list
        And print the "Walk the dog successfully removed"

    Scenario: Add new Remove task error handling
        Given the terminal is opened in the project
        When the application is run with the '-r' argument
        Then it should show an error message like "Unable to remove: no index provided"
    Scenario: Add new Remove task error handling
        Given the terminal is opened in the project
        When the application is run with the '-r20' argument
        Then it should show an error message like "Unable to remove: index is out of bound"

    Scenario: Add new Remove task error handling
        Given the terminal is opened in the project
        When the application is run with the '-r apple' argument
        Then it should show an error message like "Unable to remove: index is not a number"

    Scenario: Add new Argument error handling
        Given the terminal is opened in the project
        When the application is run with unsupported argument
        Then it should show an error message like "Unsupported argument"

    Scenario: Add Check task
        Given the terminal is opened in the project And the file has at least 2 tasks
        When the application is run with ""-c 2" argument
        Then it should  it should check the second task from the file

