from google.cloud import resource_manager

def get_gcp_project_info():
    """Lists GCP projects and prints their ID and name."""

    client = resource_manager.Client()
    projects = client.list_projects()

    print("GCP Projects:")
    for project in projects:
        print(f"  Project ID: {project.project_id}, Name: {project.name}")

if __name__ == "__main__":
    get_gcp_project_info()