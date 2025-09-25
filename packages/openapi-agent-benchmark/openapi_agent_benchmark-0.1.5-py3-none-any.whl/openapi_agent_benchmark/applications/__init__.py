from openapi_agent_benchmark.applications.base import Application


def get_applications(owner: str, repo: str) -> list[Application]:
    applications = [
        Application(
            owner='coollabsio',
            repo='coolify',
            version='v4.0.0-beta.407',
            commit_hash='c87d12d77381e708a10cdc0b2bb5ceda04eb9006',
        ),
        Application(
            owner='koel',
            repo='koel',
            version='v7.2.2',
            commit_hash='fa765a0b0ab0a6f7fa0f2270fdbe3ecb6724d820',
        ),
        Application(
            owner='kimai',
            repo='kimai',
            version='2.32.0',
            commit_hash='9ca69e11140deb1da6b2756d931b449beca7880d',
        ),
        Application(
            owner='part-db',
            repo='part-db-server',
            version='v1.17.0',
            commit_hash='60ab992360f177826759846bb4e525286af11e08',
        ),
    ]
    return [application for application in applications if application.owner == owner and application.repo == repo]
