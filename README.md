# Teachers Management Web Application

## Overview

This project is a web application for managing teachers, their work records, salary reports, and student information. It is built primarily in Python using the Django framework for the backend, and HTML, CSS, and JavaScript for the frontend.

## Features

- Worker authentication and dashboard
- Record and view work logs 
- Generate and view worker salary reports with Portuguese date formatting
- Manage client records (add, edit, remove)
- Role-based access (worker, superuser/admin, inspector)
- Full Portuguese localization support with:
  - Portuguese date format (dd/mm/yyyy)
  - Europe/Lisbon timezone
  - Portuguese translations for all user interface elements
- Superusers can:
  - Open and delete client and worker accounts
  - Create, edit, and remove taxes and services
  - Perform billing
  - Record work sessions for workers
  - Calculate worker salaries
  - Generate and update salary reports for workers
    - Creating a new salary report for a period will replace any existing report for that period
    - Changes to prices or worker rates will not affect previously generated bills or salary reports; historical values are preserved for accurate record-keeping
  - **Bulk Bill All Clients:** Generate bills for all clients for a selected month in one click, with a preview and options to update or skip existing bills. Prevents double billing and allows reviewing actions before confirming.
  - **Bulk Salary Reports for All Workers:** Create or update salary reports for all workers for a selected month in one click, with a preview and options to update or skip existing reports. Paid reports require explicit confirmation to update. Supervisor can select any month/year.
  - **Flexible Month/Year Selection:** On both bulk billing and salary reporting, select any month and year before previewing or confirming the operation. Default is previous month, but supervisor can generate reports at any time.
  - **Dashboard Shortcuts:** Prominent buttons for both bulk billing and bulk salary reports are available in the left column of the superuser dashboard for quick access.
- Inspectors can:
  - View all work sessions (for any worker)
  - View all bills (for any client)
  - View all salary reports (for any worker)
  - View all client and worker records
  - Inspectors **cannot** add, edit, or delete any data (read-only access)
- Workers can:
  - Record work sessions for themselves and view them
    - (This feature can be deactivated for some organizations)
  - View their own salary reports
  - Export work records to CSV for reporting purposes
  - Generate PDF reports of their work history
    - Export work history to Excel for detailed analysis
- Clients can:
  - View their own bills
  - Edit their own contact information (telephone, email)

## Flowcharts & Visual Guides

### 1. User Roles & Permissions

```mermaid
flowchart TD
    A[Superuser] -- Can View & Edit --> B[Work Sessions]
    A -- Can View & Edit --> C[Bills]
    A -- Can View & Edit --> D[Salary Reports]
    A -- Can View & Edit --> E[Students]
    A -- Can View & Edit --> F[Teachers]
    
    G[Inspector] -- Can View Only --> B
    G -- Can View Only --> C
    G -- Can View Only --> D
    G -- Can View Only --> E
    G -- Can View Only --> F
    
    H[Teacher] -- Can View & Record Own --> B
    H -- Can View Own --> D
    
    I[Student] -- Can View Own --> C
    I -- Can Edit Own Contact --> E
```

### 2. Billing Process Flowchart

```mermaid
flowchart TD
    StartBilling[Start Billing Process]
    SelectMonth[Select Month/Year]
    ChooseStudent[Choose Student]
    PreviewBills[Preview Bills]
    ConfirmBilling{Confirm Billing}
    GenerateBills[Generate Bills]
    Notify[Notify Students]
    EndBilling[End]

    StartBilling --> SelectMonth
    SelectMonth --> ChooseStudent
    ChooseStudent --> PreviewBills
    PreviewBills --> ConfirmBilling
    ConfirmBilling -- Yes --> GenerateBills
    GenerateBills --> Notify
    Notify --> EndBilling
    ConfirmBilling -- No --> EndBilling
  ```

### 3. Salary Report Generation Flowchart

```mermaid
flowchart TD
    StartSalary[Start Salary Report Generation]
    SelectPeriod[Select Month/Year]
    ChooseTeacher[Choose Teacher]
    PreviewReports[Preview Reports]
    ConfirmReports{Confirm Generation}
    GenerateReports[Generate Salary Reports]
    NotifyTeachers[Notify Teachers]
    EndSalary[End]

    StartSalary --> SelectPeriod
    SelectPeriod --> ChooseTeacher
    ChooseTeacher --> PreviewReports
    PreviewReports --> ConfirmReports
    ConfirmReports -- Yes --> GenerateReports
    GenerateReports --> NotifyTeachers
    NotifyTeachers --> EndSalary
    ConfirmReports -- No --> EndSalary
```

## Tech Stack

- **Backend:** Python (Django)
- **Frontend:** HTML, CSS, JavaScript (Django templating)
- **Database:** SQLite (default, can be switched to PostgreSQL/MySQL)
- **Internationalization:**
  - Portuguese (pt-pt) language support
  - Custom date formatting for Portuguese users
  - Europe/Lisbon timezone configuration

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/workers.git
   cd workers
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000`

## Folder Structure

- `templates/` - HTML templates
- `static/` - Static files (CSS, JS, images)
- `workers/` - Main Django app
- `manage.py` - Django project entry point
- `requirements.txt` - Python dependencies

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

## License

To be decided. The license for this project has not been chosen yet.
