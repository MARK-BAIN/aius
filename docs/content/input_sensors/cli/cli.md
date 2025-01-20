# Input sensors -> CLI

The AIUS CLI (command-line interface) console is a type of sensor that serves two purposes:

1. You can execute commands like:
- `poetry run aius` to see all high-level utility commands
- or `poetry run aius agents list` to preview all your agents
- or create agents
    ```bash
    aius agents create --name "Agent 0" \
    --goals = ["Take care of yourself", "Act to stay in control", "Grow your community"]
    --sensors ["cli"] \
    --memory ["wm-ram","stm-kv","entity-vector","ltm-graph"] \
    --processing ["lm.groq.llama3-70b-8192","embed.open_click.ViT-H-14"] \
    --tools ["cli","exa_search"]
    ```
2. As shown above, you can use it for any of your agents as one of the sensing interfaces or output tools.

---

### AIUS CLI reference
To start the AIUS CLI from terminal run:
  ```bash
  poetry run aius
  ```

---

##### Agents
To work with **Agents** use the `aius agents` utility
```bash
aius agents list
aius agents create OPTIONS
aius agents sleep {agent_ids} OPTIONS
aius agents wake {agent_ids} OPTIONS
aius agents kill {agent_ids} OPTIONS
```

---

##### Input_sensors
To work with **Input_sensors** use the `aius sensors` utility
```bash
aius sensors list
aius sensors create OPTIONS
aius sensors sleep {ids} OPTIONS
aius sensors wake {ids} OPTIONS
aius sensors kill {ids} OPTIONS
```

---

##### Log_memory
To work with **Log_memory** use the `aius memory` utility
```bash
aius memory list
aius memory create OPTIONS
aius memory sleep {ids} OPTIONS
aius memory wake {ids} OPTIONS
aius memory kill {ids} OPTIONS
```

---

##### Log_processing
To work with **Log_processing** use the `aius processing` utility
```bash
aius processing list
aius processing create OPTIONS
aius processing sleep {ids} OPTIONS
aius processing wake {ids} OPTIONS
aius processing kill {ids} OPTIONS
```

---

##### Output_tools
To work with **Output_tools** use the `aius tools` utility
```bash
aius tools list
aius tools create OPTIONS
aius tools sleep {ids} OPTIONS
aius tools wake {ids} OPTIONS
aius tools kill {ids} OPTIONS
```

---

> 💬 Ask questions or discuss **CLI** with others on [Discord](https://discord.gg/cM6vFhJbWS)