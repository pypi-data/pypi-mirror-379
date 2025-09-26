import api from "./api_client.js"; // import axios instance

document.addEventListener("DOMContentLoaded", () => {
    const logDate = document.getElementById("logDate");
    const fileSelect = document.getElementById("fileSelect");
    const startTime = document.getElementById("startTime");
    const endTime = document.getElementById("endTime");
    const uuidFilter = document.getElementById("uuidFilter");
    const tabsDiv = document.getElementById("tabs");

    logDate.valueAsDate = new Date();

    // Load files for selected date
    document.getElementById("fetchFiles").addEventListener("click", async () => {
        if (!logDate.value) return alert("Date is mandatory");
        try {
            const res = await api.get(`/logs/files`, { params: { date: logDate.value } });
            const data = res.data;
            fileSelect.innerHTML = "";
            data.files.forEach(f => {
                const opt = document.createElement("option");
                opt.value = f;
                opt.innerText = f;
                fileSelect.appendChild(opt);
            });
        } catch (err) {
            console.error(err);
            alert("Failed to load files");
        }
    });

    // Fetch logs
    document.getElementById("fetchLogs").addEventListener("click", async () => {
        const uuid = uuidFilter.value.trim();
        const selectedFiles = Array.from(fileSelect.selectedOptions).map(o => o.value);
        const start = startTime.value;
        const end = endTime.value;

        if (start && end && start > end) {
            return alert("Start time cannot be greater than End time");
        }

        if (!logDate.value || !start || !end && !uuid) return alert("Date and time range are mandatory");
        if (!logDate.value || !start || !end) {
            if(!uuid) return alert("Select at least one file or provide UUID");
        }


        try {
            const params = new URLSearchParams();
            params.append("date", logDate.value);
            selectedFiles.forEach(f => params.append("files", f));
            params.append("start_time", start);
            params.append("end_time", end);
            if (uuid) params.append("uuid", uuid);

            const res = await api.get(`/logs/logs_by_files?${params.toString()}`);
            const data = res.data;

            tabsDiv.innerHTML = "";
            Object.keys(data.logs).forEach(file => {
                const tab = document.createElement("div");
                tab.classList.add("bg-white", "p-4", "rounded", "shadow", "mb-4");
                tab.innerHTML = `<h3 class="font-semibold mb-2">${file}</h3><pre class="font-mono text-sm overflow-x-auto">${data.logs[file].join("\n")}</pre>`;
                tabsDiv.appendChild(tab);
            });
        } catch (err) {
            console.error(err);
            alert("Failed to fetch logs");
        }
    });

    // Download logs
    document.getElementById("downloadLogs").addEventListener("click", () => {
        const uuid = uuidFilter.value.trim();
        const selectedFiles = Array.from(fileSelect.selectedOptions).map(o => o.value);
        if (!uuid && selectedFiles.length === 0) return alert("Select at least one file or provide UUID");

        const params = new URLSearchParams();
        params.append("date", logDate.value);
        selectedFiles.forEach(f => params.append("files", f));
        const url = `/logs/download_logs?${params.toString()}`;
        window.open(url, "_blank");
    });
});
