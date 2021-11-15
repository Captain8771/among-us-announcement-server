# THIS IS NOT A MOD
## Custom Among Us Announcement Server
note: this **WILL** need a mod to function.

setup:
- change the `app.announcement` variable and the port (if needed)
- create a mod changing the `Constants.BaseEndpoint` variable to `https://<yourip>:<port>/api/`
    - NOTE: it is recommended to do this on announcement fetch, and changing it back after.
    - when i was writing this i was running into issues with the among us cache, my solution was to simply remove the among us announcement caching
