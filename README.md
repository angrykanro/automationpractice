# How to start tests:
1. Install docker and docker compose
1. Start containers inside repo root folder:```docker-compose up```
1. Open in browser http://localhost:3000/
1. Press button **Start tests**
1. Refresh page to see the results

# How to see screenshots from failed tests
1. From inside repo root directory type ```docker exec -ti automationpractice_api_1 bash```
1. Type ```mv %screentshot_path% .```
1. Open screenshot
