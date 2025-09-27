import sys

import uvicorn
from fastapi import BackgroundTasks, FastAPI, Header, Request

app = FastAPI()


@app.post("/")
async def receive_payload(
    request: Request,
    background_tasks: BackgroundTasks,
    x_github_event: str = Header(...),
):
    match x_github_event:
        case "create":
            payload = await request.json()
            ref = payload.get("ref")
            repository = payload.get("repository", {}).get("full_name")
            background_tasks.add_task(deploy, repository, ref)

            return {
                "message": f"Deployment on {repository} for tag {ref} started."
            }
        case "ping":
            return {"message": "pong"}
        case _:
            return {
                "message": f"Event {x_github_event} received. No action taken."
            }


def deploy(repository: str, ref: str) -> None:
    # Simulate deployment process
    print(f"Deploying {repository} at ref {ref}...")
    # Here you would add the actual deployment logic
    print(f"Deployment of {repository} at ref {ref} completed.")


def main() -> None:
    """
    Main entry point for running the FastAPI application.

    when --uds is passed it takes the next argument as the socket path
    when --host and --port are passed it takes the next two arguments as
    host and port

    Example:
        gancho --host 127.0.0.1 --port 5000
        gancho --uds /path/to/socket

    when nothing is passed it defaults to 127.0.0.0 and port 5000
    """
    args = sys.argv[1:]

    if "--uds" in args:
        uds_index = args.index("--uds") + 1

        if uds_index < len(args):
            uds_path = args[uds_index]
            uvicorn.run(app, uds=uds_path, log_level="info")
    elif "--host" in args and "--port" in args:
        host_index = args.index("--host") + 1
        port_index = args.index("--port") + 1

        if host_index < len(args) and port_index < len(args):
            host = args[host_index]
            port = int(args[port_index])
            uvicorn.run(app, host=host, port=port, log_level="info")
    else:
        uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
