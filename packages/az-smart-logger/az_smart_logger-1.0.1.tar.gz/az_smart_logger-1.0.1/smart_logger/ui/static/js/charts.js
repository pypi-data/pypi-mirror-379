import api from "./api_client.js"; // axios instance

let dayChart, monthChart, yearChart;

const daySelector = document.getElementById("daySelector");
const monthSelector = document.getElementById("monthSelector");
const yearSelector = document.getElementById("yearSelector");

const ctxDay = document.getElementById("dayChart").getContext("2d");
const ctxMonth = document.getElementById("monthChart").getContext("2d");
const ctxYear = document.getElementById("yearChart").getContext("2d");

function createChart(ctx, labels, data, label, bgColor='rgba(59, 130, 246, 0.7)'){
    return new Chart(ctx, {
        type: 'bar',
        data: { labels, datasets: [{ label, data, backgroundColor: bgColor }] },
        options: { responsive: true, plugins: { legend: { display: false } } }
    });
}

// -------- Fetch and render day-wise error type chart --------
async function renderDayChart(date){
    if(!date) return;
    try{
        const res = await api.get("/logs/daywise_by_type", { params: { date } });
        const data = res.data.logs;
        const labels = Object.keys(data);
        const counts = Object.values(data);
        if(dayChart) dayChart.destroy();
        dayChart = createChart(ctxDay, labels, counts, `Logs by Type (${date})`, 'rgba(220, 38, 38,0.7)');
    }catch(err){ console.error(err); }
}

// -------- Fetch and render month-wise day chart --------
async function renderMonthChart(month){
    if(!month) return;
    try{
        const res = await api.get("/logs/monthwise", { params: { month } });
        const data = res.data.logs;
        const labels = Object.keys(data);
        const counts = Object.values(data);
        if(monthChart) monthChart.destroy();
        monthChart = createChart(ctxMonth, labels, counts, `Logs per Day (${month})`, 'rgba(34, 197, 94,0.7)');
    }catch(err){ console.error(err); }
}

// -------- Fetch and render year-wise month chart --------
async function renderYearChart(year){
    if(!year) return;
    try{
        const res = await api.get("/logs/yearwise", { params: { year } });
        const data = res.data.logs;
        const labels = Object.keys(data);
        const counts = Object.values(data);
        if(yearChart) yearChart.destroy();
        yearChart = createChart(ctxYear, labels, counts, `Logs per Month (${year})`, 'rgba(59, 130, 246,0.7)');
    }catch(err){ console.error(err); }
}

// -------- Event listeners --------
daySelector.addEventListener("change", () => renderDayChart(daySelector.value));
monthSelector.addEventListener("change", () => renderMonthChart(monthSelector.value));
yearSelector.addEventListener("change", () => renderYearChart(yearSelector.value));

// -------- Initial render --------
const today = new Date();
daySelector.valueAsDate = today;
monthSelector.value = today.toISOString().slice(0,7);
yearSelector.value = today.getFullYear();

renderDayChart(daySelector.value);
renderMonthChart(monthSelector.value);
renderYearChart(yearSelector.value);


export { renderDayChart, renderMonthChart, renderYearChart };