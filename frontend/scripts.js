document.getElementById('send-btn').addEventListener('click', function () {
    const userInput = document.getElementById('user-input').value;
  
    if (userInput) {
      // Append user message to chatbox
      appendMessage('user', userInput);
  
      // Send user input to Rasa backend
      sendMessageToRasa(userInput);
  
      // Clear input field
      document.getElementById('user-input').value = '';
    }
  });
  
  function appendMessage(sender, message) {
    const chatBox = document.getElementById('chat-box');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('chat-message');
  
    if (sender === 'bot') {
      messageDiv.classList.add('bot-message');
    } else {
      messageDiv.classList.add('user-message');
    }
  
    messageDiv.innerText = message;
    chatBox.appendChild(messageDiv);
  
    // Scroll chat box to the bottom
    chatBox.scrollTop = chatBox.scrollHeight;
  }
  
  async function sendMessageToRasa(message) {
    try {
      const response = await fetch('http://localhost:5005/webhooks/rest/webhook', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          sender: 'user', // Unique identifier for each user
          message: message,
        }),
      });
  
      const botResponses = await response.json();
  
      botResponses.forEach((botResponse) => {
        appendMessage('bot', botResponse.text);
      });
    } catch (error) {
      console.error('Error sending message to Rasa:', error);
    }
  }
  