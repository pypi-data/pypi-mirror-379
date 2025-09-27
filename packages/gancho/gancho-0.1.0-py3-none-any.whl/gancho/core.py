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
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
