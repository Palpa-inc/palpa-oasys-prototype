<script setup>
const route = useRoute()
const ID = route.query.id
// fetch data
const NAME = "stuff1"
const CHATROOM_PARAM = {
    path: "/chatroom",
    query: { id: ID }
}

const TRAITS = [
    "高校受験",
    "中学英語",
    "難関校",
    "現在進行形",
    "文法",
    "単語",
    "熱血",
    "面倒見がいい",
    "丁寧"
]
</script>

<template>
    <v-row>
        <v-col xs="12" cols="12">
            <v-img src="/img/7.jpeg" cover class="text-white" aspect-ratio="1">
                <v-card-title>
                    stuff1
                </v-card-title>
            </v-img>
        </v-col>
        <v-col xs="12" cols="12">
            <v-card :title="`${NAME}の特長`">
                <v-chip v-for="i in TRAITS" class="justify-space-around">
                    {{ i }}
                </v-chip>
            </v-card>
        </v-col>
        <v-col xs="12" cols="12">
            <v-card :title="`${NAME}の評判`">

            </v-card>
        </v-col>
    </v-row>
    <v-row class="justify-align-center">
        <v-btn :to="CHATROOM_PARAM">
            このキャラと話す
        </v-btn>
    </v-row>
</template>