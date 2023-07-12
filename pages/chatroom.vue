<script setup>
import axios from 'axios';
import { ref, reactive } from 'vue';

const newMessage = ref('');
const isLoading = ref(false);
const message_stack = reactive([
  {
    "role": "system",
    "content": "Hi"
  }
])
async function postChat() {
  if (!isLoading.value && newMessage.value.trim() !== '') {
    isLoading.value = true;
    const userMessage = {content: newMessage.value, role: "user"};
    message_stack.push(userMessage);
    newMessage.value = "";
    const loadingMessage = {content: '入力中...', role: "system"};
    message_stack.push(loadingMessage);
    const { data } = await axios.post("https://palpa-prod-api.azure-api.net/api/v1/min", message_stack);
    message_stack[message_stack.length - 1] = {content: data.content, role: "system"};
    isLoading.value = false;
  }
  return data
}

</script>


<template>
  <v-container fluid class="background-container">
    <v-row justify="center">
      <v-col cols="12">
        <v-app-bar dense flat color="secondary">
          <v-toolbar-title class="chatroom-title" style="font-weight: 700; color: aliceblue;">佐藤ちあき</v-toolbar-title>
        </v-app-bar>
      </v-col>
      <v-col cols="12" class="pa-0">
        <v-card flat color="transparent">
          <v-card-text>
            <div class="chatroom-messages" ref="messagesContainer">
              <div v-for="message in message_stack" :key="message.id" class="message-wrapper"
                :class="{ 'message-left': message.role !== 'user', 'message-right': message.role === 'user' }"
                style="margin-top: 5px; margin-bottom: 5px;">
                <v-avatar v-if="message.role !== 'user'" size="48">
                  <v-img src="/palpa-oasys-prototype/img/0.jpeg" alt="Bob's Icon"></v-img>
                  <!-- <v-img src="/img/0.jpeg" alt="Bob's Icon"></v-img> -->
                </v-avatar>
                <div
                  :class="{ 'message-content-left': message.role !== 'user', 'message-content-right': message.role === 'user' }"
                  style="padding-top: 20px; padding-bottom: 20px; font-size:large;">
                  <span v-if="!message.loading" class="message-sender">{{ message.content }}</span>
                  <span v-else class="message-sender loading">{{ message.content }}</span>
                </div>
              </div>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <div class="chat-input-area">
      <input ref="messageInput" v-model="newMessage" class="chat-input" placeholder="Type your message"
        @keydown.enter.meta="postChat(newMessage)"
        
        :class="{ 'loading': isLoading }">
      <button class="chat-send-button" @click="postChat(newMessage)" :disabled="isLoading">Send</button>
    </div>
  </v-container>
</template>
  
<style scoped>
.background-container {
  background-image: url("/palpa-oasys-prototype/img/background.jpeg");
  /* background-image: url("/img/background.jpeg"); */
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

.loading::after {
  content: '...';
  animation: loading 1s steps(3, end) infinite;
}

@keyframes loading {
  0% { opacity: 0; }
  50% { opacity: 1; }
  100% { opacity: 0; }
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
  
  