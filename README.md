# quake_log

The idea is to create a log_parser application/service based on clean arch so we can have our application with each component working indivually and ready if we need to chagen frameworks and so on.

Explanation of the folder structure:

src/: This is where the main source code for your application resides.

- app/: Contains the core application code.
- controllers/: API controllers responsible for handling requests and responses.
- use_cases/: Application use cases, like parsing the log file.
- entities/: Core domain entities.
- repositories/: Interfaces for data repositories (implementations can be in the "adapters" folder).
- config.py: Configuration and settings for the application.
- adapters/: Contains adapters that connect the application to external resources (gateways).
- gateways/: Implementations of data gateways, like the file system gateway.
- interfaces/: Contains interfaces that define how the application interacts with external components.
- api/: Defines API routes.
- persistence/: Defines the repository interface.
- tests/: Contains test cases.
- unit/: Unit tests for different components.
- Follows a similar structure as the "src/app" folder.
- requirements.txt: List of required Python packages.
- README.md: Project documentation.
- app.py: Main application entry point

The idea is to keep it as simple as possible and at same time more prepared as possible to be able to grow or change integrations, databases(in our case there is no database but is ready in case we want to integrate to one)

installing and using:
because of the simplicity you only need python, and flask installed for tests I used pytest.

pip install flask

python app.py

curl http://localhost:5000/games
