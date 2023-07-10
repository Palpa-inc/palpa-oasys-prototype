<template >
    <div class="pt-2 background-container" style="padding-top: 100%;">
        <!-- フレンズ -->
        <v-row justify="center" class="pa-2" style="margin-top: 10px;">
            <v-card v-ripple flat class="px-50 py-5 text-center"
                style="border-radius: 30px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); padding: 10% 5%; margin-top: 10%;">
                <a>
                    フレンズ
                </a>
                <h1 style="font-size: 40px; font-weight: bold; color: #333;">
                    Friends
                </h1>
            </v-card>
        </v-row>

        <v-row style="margin-top: 30px;">
            <v-col>
                <v-card flat class="justify-center pa-2 text-center">
                    <h2>
                        お気に入りのキャラで<br>あなたの学習を支援
                    </h2>
                </v-card>
            </v-col>
        </v-row>

        <v-row class="py-10">
            <v-col cols="12" class="text-center">
                <v-divider vertical :length="100"
                    style="border-width: 1.5px; height: 200px; width: 100px; border-color:#000000"></v-divider>
            </v-col>
        </v-row>

        <v-row>
            <v-col class="justify-center pa-2 text-center" style="margin-bottom: 30px;">
                <h2>
                    フレンズを探す
                </h2>
            </v-col>
        </v-row>

        <v-row class="pa-4 justify-content-start" no-gutters style="row-gap: 1em;  column-gap: 0em;">
            <v-col xs="6" md="6" lg="4" v-for="(i, index) in friends" class="ma-0 pa-4 col position-relative"
                style="flex-grow: 10; margin:10%; column-gap: 100px; width: 400px;">
                <v-card class="mx-auto d-flex flex-column" style="height: 500px; width: 300px; border-radius: 20px;">
                    <v-img :src="`/palpa-oasys-prototype/img/${index}.jpeg`" cover class="text-white align-end text-white flex-grow-1">
                    </v-img>
                    <v-card flat class="pa-2 position-absolute d-flex flex-column justify-content-between"
                        :style="{ backgroundColor: i.color }"
                        style=" bottom: 0; left: 0; right: 0;  border-radius: 15px; padding: 0; margin: 10px"
                        :to="friend_route(i.id)">
                        <v-card-title
                            style="color: #FFFFFF; font-weight: 700; font-size:x-large; display: flex; justify-content: space-between;">
                            <span>{{ i["name"] }}</span>
                            <span style="margin-left: auto;">>></span>
                        </v-card-title>
                        <v-col class="d-flex flex-wrap">
                            <v-chip v-for="tag in i.tags" :color="tagColor(tag)" dark :key="tag" class="ma-1"
                                style="font-weight: 500; background: #ffffff; border-radius: 5px;">
                                {{ tag }}
                            </v-chip>
                        </v-col>
                        <!-- <v-btn color="primary" style="height: 40px; border-radius: 25px;"  :to="friend_route(i.id)">
                            詳しく
                        </v-btn> -->
                    </v-card>
                </v-card>
            </v-col>
        </v-row>
    </div>
</template>
  
<script setup>
const friend_route = function (id) { return { path: "/character", query: { id } } }
const friends = [
    {
        id: "stuff1",
        name: "佐藤ちあき",
        tags: [
            "学習支援",
            "英語",
            "高校受験"
        ],
        color: "#7AA1B899"
    },
    {
        id: "stuff2",
        name: "橘みれい",
        tags: [
            "学習支援",
            "英語",
            "高校受験"
        ],
        color: "#211E2699"
    },
    {
        id: "stuff3",
        name: "瀬名たくと",
        tags: [
            "学習支援",
            "英語",
            "高校受験"
        ],
        color: "#3054AA99"
    },
    {
        id: "stuff4",
        name: "瀬名たくと",
        tags: [
            "学習支援",
            "英語",
            "高校受験"
        ],
        color: "#FB989799"
    }
]
function tagColor(tag) {
    const obj = {
        "学習支援": "green",
        "英語": "orange",
        "高校受験": "blue"
    };
    return obj[tag]
}
</script>
  
<style>
.background-container {
  background-image: url("/palpa-oasys-prototype/img/background.jpeg");
  background-size: cover;
  background-repeat:no-repeat;
  background-position:center;
}
</style>