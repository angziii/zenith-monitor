const focusScoreEl = document.getElementById('focus-score');
const statusTextEl = document.getElementById('status-text');
const activeAppEl = document.getElementById('active-app');
const faceStatusEl = document.getElementById('face-status');
const alertBanner = document.getElementById('alert-banner');
const circle = document.querySelector('.progress-ring__circle');

const radius = circle.r.baseVal.value;
const circumference = radius * 2 * Math.PI;

circle.style.strokeDasharray = `${circumference} ${circumference}`;
circle.style.strokeDashoffset = circumference;

function setProgress(percent) {
    const offset = circumference - (percent / 100) * circumference;
    circle.style.strokeDashoffset = offset;
    
    // Color transition
    if (percent > 70) {
        circle.style.stroke = '#00d2ff';
    } else if (percent > 40) {
        circle.style.stroke = '#f1c40f';
    } else {
        circle.style.stroke = '#ff2e63';
    }
}

async function updateStatus() {
    try {
        const response = await fetch('http://localhost:8000/status');
        const data = await response.json();

        focusScoreEl.textContent = Math.round(data.focus_score);
        setProgress(data.focus_score);

        activeAppEl.textContent = data.active_app || 'N/A';
        faceStatusEl.textContent = data.face_detected ? 'CONNECTED' : 'NOT DETECTED';
        
        if (data.is_slacking) {
            statusTextEl.textContent = 'SLACKING';
            statusTextEl.style.color = '#ff2e63';
            alertBanner.classList.remove('hidden');
        } else {
            statusTextEl.textContent = 'FOCUSED';
            statusTextEl.style.color = '#00d2ff';
            alertBanner.classList.add('hidden');
        }

    } catch (error) {
        console.error('Failed to fetch status:', error);
        statusTextEl.textContent = 'OFFLINE';
        statusTextEl.style.color = '#7f8c8d';
    }
}

// Initial update
updateStatus();

// Polling interval
setInterval(updateStatus, 1000);
