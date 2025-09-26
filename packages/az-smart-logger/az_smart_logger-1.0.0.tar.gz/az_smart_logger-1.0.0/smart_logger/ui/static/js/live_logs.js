document.addEventListener("DOMContentLoaded", function() {
    // Get terminal div
    const terminal = document.getElementById('logsTerminal');

    // Get token from localStorage
    const token = localStorage.getItem("token");
    console.log("Token:", token);
    if (!token) {
        window.location.href = "/auth/login";
        return;
    }

    // Connect to Socket.IO server with namespace
    const socket = io("http://127.0.0.1:8000/live_event_logs", {
        path: "/socket.io",             // must match backend ASGIApp socketio_path
        transports: ["websocket"],      // force websocket transport
        query: { token },               // send JWT token
    });

    console.log("Connecting to WebSocket server...", socket);

    // Connection event
    socket.on("connect", () => {
        const div = document.createElement('div');
        div.innerText = "[INFO] Connected to live_event_logs";
        div.classList.add("text-green-400");
        terminal.appendChild(div);
        console.log("[DEBUG] Connected with SID:", socket.id);
    });

    // Receive log events from backend (generic message)
    socket.on("message", (log) => {
        const div = document.createElement('div');
        console.log("Received log:", log);
        switch(log.log_type) {
            case "INFO": div.classList.add("text-green-400"); break;
            case "WARNING": div.classList.add("text-yellow-300"); break;
            case "ERROR": div.classList.add("text-red-500"); break;
            case "CRITICAL": div.classList.add("text-red-800", "font-bold"); break;
            default: div.classList.add("text-white");
        }

        div.innerText = `[${log.timestamp}] [${log.log_type}] ${log.message}`;
        terminal.appendChild(div);

        // Auto scroll
        terminal.scrollTop = terminal.scrollHeight;

        // Keep last 200 logs
        if (terminal.children.length > 200) terminal.removeChild(terminal.firstChild);
    });

    socket.on("log_event", (log) => {
        const div = document.createElement('div');
        div.classList.add("text-sm", "font-mono");
        const msg = log.msg || "";  // backend se msg property

        // Extract log_type from line, assuming format: "[uuid] [LOG_TYPE] ..."
        const match = msg.match(/\[([A-Z]+)\]/);
        let logType = "INFO";
        if (match && match[1]) {
            logType = match[1];
        }

        switch(logType) {
            case "INFO": div.classList.add("text-green-400"); break;
            case "WARNING": div.classList.add("text-yellow-300"); break;
            case "ERROR": div.classList.add("text-red-500"); break;
            case "CRITICAL": div.classList.add("text-red-800", "font-bold"); break;
            default: div.classList.add("text-white");
        }

        div.innerText = msg;  // pura line
        terminal.appendChild(div);

        // Auto scroll
        terminal.scrollTop = terminal.scrollHeight;

        // Keep last 200 logs
        if (terminal.children.length > 200) terminal.removeChild(terminal.firstChild);
    });


    // Handle disconnect
    socket.on("disconnect", (reason) => {
        const div = document.createElement('div');
        div.innerText = `[INFO] Disconnected. Reason: ${reason}. Reconnecting...`;
        div.classList.add("text-yellow-300");
        terminal.appendChild(div);
    });
});
