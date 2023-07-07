<script setup lang="ts">
import { ref } from 'vue'
const TITLE = "Prototype 1"
let drawer = ref(false)
const NAVIGATION_ITEMS = [
    {
        title: "this",
    },
    {
        title: "that",
    }
]
</script>

<template>
    <v-layout class="rounded rounded-md">
        <v-app-bar color="teal-darken-4" image="https://picsum.photos/1920/1080?random">
            <template v-slot:image>
                <v-img gradient="to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)"></v-img>
            </template>

            <template v-slot:prepend>
                <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
            </template>

            <v-app-bar-title>{{ TITLE }}</v-app-bar-title>
        </v-app-bar>
        <v-navigation-drawer v-model="drawer" @click="rail = false">
            <v-list nav>
                <v-list-item prepend-icon="mdi-home-city" title="Home" value="home"></v-list-item>
                <v-list-item prepend-icon="mdi-account" title="My Account" value="account"></v-list-item>
                <v-list-item prepend-icon="mdi-account-group-outline" title="Users" value="users"></v-list-item>
            </v-list>
        </v-navigation-drawer>
        <v-main>
            <slot></slot>
        </v-main>
    </v-layout>
</template>