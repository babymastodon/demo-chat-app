document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('message-input');
    const sendBtn = document.getElementById('send-btn');
    const chatLog = document.getElementById('chat-log');

    function appendMessage(sender, text) {
        const msgDiv = document.createElement('div');
        msgDiv.classList.add('mb-2');
        const userClass = sender === 'bot' ? 'text-primary' : 'text-success';
        msgDiv.innerHTML = `
          <span class="fw-bold ${userClass}">${sender}:</span>
          <span>${text}</span>
        `;
        chatLog.appendChild(msgDiv);
        chatLog.scrollTop = chatLog.scrollHeight;
    }

    sendBtn.addEventListener('click', () => {
        const msg = input.value.trim();
        if (!msg) return;
        appendMessage('user', msg);
        input.value = '';
        fetch('/send_message', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: msg })
        })
        .then(res => res.json())
        .then(data => {
            if (data.response) appendMessage('bot', data.response);
        });
    });

    input.addEventListener('keyup', (e) => {
        if (e.key === 'Enter') sendBtn.click();
    });
});
