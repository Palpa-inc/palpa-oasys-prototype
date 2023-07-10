<script setup>
const route = useRoute()
const ID = route.query.id
// fetch data
const NAME = "佐藤ちあき"
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
    <v-row style="background-color: #6694ad;">
        <v-col xs="12" cols="12">
            <v-img src="/palpa-oasys-prototype/img/0.jpeg" cover class="text-white" aspect-ratio="1" style="width: 100%; position: fixed;">
                <v-card-title style="font-weight: 900; padding-top: 20px;">
                    {{ NAME }}
                </v-card-title>
            </v-img>
        </v-col>
        <v-col class="d-flex justify-center align-center" xs="12" cols="12" style="width: 50%; padding: 20px; padding-top: 300px;">
            <v-card class="pa-2 ma-2 justify-content-center" flat style="width: 250vw; background-color: #FFFFFF99; border-radius: 20px; ">
                <h1 style="padding: 20px; font-size: xx-large;">
                    「誠実な努力が一番の近道なの」
                </h1>
                <p style="font-size: 25px; font-size: large; padding: 20px;">
                    公立高校の生徒会長であり、学校のアイドルでもある千晶はそう言った。名声を求める密かな気持ちが、困っている人を助けたいという彼女の気持ちを形作ってきた。高校の学校説明会であなたと知り合った彼女は、あなたの英語学習をサポートさせてほしいと言う。
                </p>
            </v-card>
        </v-col>
        <v-col xs="12" cols="12" class="d-flex justify-center align-center" style="width: 50%; padding: 25px;">
            <v-card flat class="pa-2" style="width: 250vw; background-color: #FFFFFF99; border-radius: 20px;">
                <v-card-title class="text-center" style="font-weight:800; font-size: x-large;">
                {{ `${NAME}の特長` }}
                </v-card-title>
                <v-col class="d-flex flex-wrap">
                    <v-chip v-for="i in TRAITS" dark class="ma-2 pa-6" style="font-size: large; font-weight: 500; background: #ffffff; border-radius: 5px; padding: 20px;">
                        {{ i }}
                    </v-chip>
                </v-col>
            </v-card>
        </v-col>

        <!-- <v-col xs="12" cols="12">
            <v-card :title="`${NAME}の評判`" flat class="pa-2" />
        </v-col> -->
    </v-row>
    
    <v-row class="justify-center" style="width: 100%; padding: 0px; padding-bottom: 40px;">
        <v-col cols="12" md="12" class="d-flex justify-center" style="margin-left: 25px;" >
            <v-btn :to="CHATROOM_PARAM" block style="width:100%; max-width: 800px; height:60px; background-color: #6694ad; color: #ffffff; font-size: x-large; font-weight: 900; border-radius: 10px;">
            このキャラと話す
            </v-btn>
        </v-col>
    </v-row>
</template>