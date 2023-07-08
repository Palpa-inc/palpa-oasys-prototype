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
            <v-img src="/palpa-oasys-prototype/img/7.jpeg" cover class="text-white" aspect-ratio="1">
                <v-card-title>
                    stuff1
                </v-card-title>
            </v-img>
        </v-col>
        <v-col xs="12" cols="12">
            <v-card class="pa-2" flat>
                <h2>
                    「誠実な努力が一番の近道なの」
                </h2>
                <p>
                    公立高校の生徒会長であり、学校のアイドルでもある千晶はそう言った。名声を求める密かな気持ちが、困っている人を助けたいという彼女の気持ちを形作ってきた。高校の学校説明会であなたと知り合った彼女は、あなたの英語学習をサポートさせてほしいと言う。
                </p>
            </v-card>
        </v-col>
        <v-col xs="12" cols="12">
            <v-card :title="`${NAME}の特長`" flat class="pa-2">
                <v-chip v-for="i in TRAITS" class="justify-space-around">
                    {{ i }}
                </v-chip>
            </v-card>
        </v-col>
        <v-col xs="12" cols="12">
            <v-card :title="`${NAME}の評判`" flat class="pa-2" />
        </v-col>
    </v-row>
    <v-row class="justify-align-center">
        <v-btn :to="CHATROOM_PARAM" block>
            このキャラと話す
        </v-btn>
    </v-row>
</template>