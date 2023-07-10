<template>
    <v-container fluid class="background-container">
      <v-row justify="center">
        <v-col cols="12">
          <v-app-bar dense flat color="secondary">
            <v-toolbar-title class="chatroom-title" style="font-weight: 700; color: aliceblue;">佐藤みちこ</v-toolbar-title>
          </v-app-bar>
        </v-col>
        <v-col cols="12" class="pa-0">
          <v-card flat color="transparent">
            <v-card-text>
              <div class="chatroom-messages" ref="messagesContainer">
                <div
                  v-for="message in messages"
                  :key="message.id"
                  class="message-wrapper"
                  :class="{'message-left': message.sender === 'Bob', 'message-right': message.sender === 'Alice'}"
                  style="margin-top: 5px; margin-bottom: 5px;"
                >
                  <v-avatar v-if="message.sender === 'Bob'" size="48">
                    <v-img src="/palpa-oasys-prototype/img/0.jpeg" alt="Bob's Icon"></v-img>
                  </v-avatar>
                  <div :class="{'message-content-left': message.sender === 'Bob', 'message-content-right': message.sender === 'Alice'}" style="padding-top: 20px; padding-bottom: 20px; font-size:large;">
                    <span class="message-sender">{{ message.content }}</span>
                  </div>
                </div>
              </div>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      <div class="chat-input-area">
            <input
                ref="messageInput"
                v-model="newMessage"
                class="chat-input"
                placeholder="Type your message"
                @keydown.enter="sendMessage"
            >
            <button class="chat-send-button" @click="sendMessage">Send</button>
        </div>
    </v-container>
  </template>
  
  <!-- 先ほどの <script> タグはそのままにしておきます -->
  
  <style scoped>
  .background-container {
    background-image: url("/palpa-oasys-prototype/img/background.jpeg");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    height: 100vh;
  }
  .chatroom {
    height: 100%;
  }

  .message-wrapper {
  display: flex;
  justify-content: flex-start;
  margin-left: 15px;
  margin-right: 15px;
  border-radius: 20px;
  padding: 20px;
  padding-right: 30px;

  }
  .message {
    display: inline-flex;
    align-items: center;
    /* font-size: large; */
    border-radius: 10px;
  }
  .message-content {
    margin-left: 10px;
  }
  .message-left {
    display: inline-flex;
    flex-direction: row;
   
  }
  .message-right {
    flex-direction: row-reverse;
  }

  .message-content-left {
    padding: 20px;
    margin-left: 15px;
    border-radius: 20px;
    background-color: #ffdde8;
  }

  .message-content-right {
    padding: 20px;
    border-radius: 20px;
    background-color: white;
  }

  .chat-input-area {
  display: flex;
  padding: 10px;
  background-color: #f5f5f5;
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
}

.chat-input {
  flex-grow: 1;
  margin-right: 10px;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.chat-send-button {
  padding: 10px 20px;
  background-color: #7FA2B5;
  color: #f5f5f5;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
  
  </style>
  
  
  
  <script>
import { ref, watch } from 'vue';

export default {
  data() {
    return {
      messages: [
        { id: 1, sender: 'Alice', content: 'Hello!' },
        { id: 2, sender: 'Bob', content: 'Hi Alice!' },
        { id: 3, sender: 'Alice', content: 'How are you?' },
        { id: 4, sender: 'Bob', content: "I'm doing well. Thanks!" },
      ],
      newMessage: '',
    };
  },
  methods: {
    sendMessage() {
      if (this.newMessage.trim() !== '') {
        this.messages.push({
          id: this.messages.length + 1,
          sender: 'Alice',
          content: this.newMessage.trim(),
        });
        
        this.newMessage = '';
      }
    },
    scrollToEnd() {
      this.$refs.messagesContainer.scrollTop = this.$refs.messagesContainer.scrollHeight;
    }
  },
  mounted() {
    this.$refs.messageInput.focus();
    this.scrollToEnd();
  },
  updated() {
    this.scrollToEnd();
  }
};
</script>
