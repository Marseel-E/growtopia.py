# User connection to server
1. User initiates connection through growtopia client.
	- User creates POST request to `www.growtopia1.com`.
	- User gets redirected to assigned server `IP` address, set through the `hosts` file.
2. Server returns `server_data.php` file.
3. File gets sent to growtopia game client.
4. User is connected to server.

```mermaid
graph TD;
    User-->Client;
    Client-->www.growtopia1.com;
    www.growtopia1.com-->server;
    server-->server_data.php;
    server_data.php-->Client;
    Client-->User;
```

```mermaid
sequenceDiagram
    User-->>Growtopia Client: Can I connect?
    Growtopia Client->>www.growtopia1.com: POST request
    Note left of www.growtopia1.com: www.growtopia1.com is <br/>mapped to our server IP
    www.growtopia1.com-->>User: server_data.php
    User->>Growtopia Client: server_data.php
    Growtopia Client-->>User: Connected!
```

# What server handles
<details><summary>Networking</summary>
Everything below but made to update to all connected peers.
</details>
<details><summary>Database</summary>

- Add data.
- Remove data.
- Update data.
</details>
<details><summary>Moving</summary>

- Jump
- Left
- Right
- Gravity
- Double Jump
- Slow Fall (/)
- Long Jump (/)
- No-Gravity. (/)
</details>
<details><summary>Worlds</summary>

- World generation.
- Locking, Ownership, Admins. (/)
- Weather effect. (/)
</details>
<details><summary>Building</summary>

- Static blocks.
- Doors. (/)
- Locks. (/)
- Signs. (/)
- Spikes. (/)
- Lava.
- Water. (/)
- Glue. (/)
- Paint. (/)
- ... (/)
</details>
<details><summary>Breaking</summary>

- Static blocks.
- Dropping seeds, gems, blocks.
- Locks.
- Water. (/)
- Fossil. (/)
</details>
<details><summary>Planting</summary>

- Planting.
- Splicing.
</details>
<details><summary>Harvesting</summary>

- Plant drops. (Gems, Seeds, Blocks, Etc...)
</details>
