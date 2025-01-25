from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sportscanner.api.routers.geolocation.endpoints import router as GeolocationRouter
from sportscanner.api.routers.venues.endpoints import router as VenuesRouter
from sportscanner.api.routers.search.badminton.endpoints import router as SearchBadmintonRouter
from sportscanner.api.routers.users.endpoints import router as UsersRouter
from datetime import datetime

description = """
Discover, Compare, and Book Sports Facilities Across London

### Sportscanner API

You will be able to:

* **Search for sports bookings and drill down using advanced filters**
* **Find available playing venues which are covered under the search**
"""

app = FastAPI(
    title="Sportscanner",
    description=description,
    summary="API to fetch sports booking availability, analytics, and advanced filters",
    version="0.0.1",
    contact={
        "name": "Yasir khalid",
        "url": "https://www.linkedin.com/in/yasir-khalid",
        "email": "yasir_khalid@outlook.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace '*' with specific origins if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(
    router= SearchBadmintonRouter,
    prefix="/search/badminton",
    tags=["Search"]
)

app.include_router(
    router= VenuesRouter,
    prefix="/venues",
    tags=["Venues"]
)

app.include_router(
    router= GeolocationRouter,
    prefix="/geolocation",
    tags=["Geolocation"]
)

app.include_router(
    router= UsersRouter,
    prefix="/users",
    tags=["Authentication"]
)

@app.get("/", tags=["Root"])
async def root():
    """Root API landing page (should be deployed at api.domain.com)"""
    return {
        "timestamp": datetime.now(),
        "message": "Welcome to the Sportscanner API",
        "actions": {
            "/search/": "Endpoint to find available sports bookings",
            "/venue/": "Endpoint to find Venues covered by Sportscanner monitoring",
            "/docs": "Documentation for API endpoints",
        }
    }

