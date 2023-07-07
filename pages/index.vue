<template>
    <div class="pt-2">
        <!-- フレンズ -->
        <v-row justify="center" class="pa-2">
            <v-card v-ripple title="Friends" flat rounded>

            </v-card>
        </v-row>

        <v-row>
            <v-col>
                <v-card flat class="justify-center pa-2">
                    <b>
                        お気に入りのキャラであなたの学習を支援
                    </b>
                </v-card>
            </v-col>
        </v-row>

        <v-row class="pa-2">
            <v-col xs="6" md="4" lg="3" v-for="i in    friends   " class="justify-space-around pa-2">
                <v-card class="mx-auto">
                    <v-img src="/img/7.jpeg" cover class="text-white align-end text-white" aspect-ratio="1">
                        <v-card-title>
                            {{ i["name"] }}
                        </v-card-title>
                    </v-img>
                    <v-card flat class="pa-2">
                        <v-row>
                            <v-col v-for="tag in i.tags">
                                <v-chip :color="tagColor(tag)" dark :key="tag">
                                    {{ tag }}
                                </v-chip>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col cols="12">
                                <v-btn color="primary" flat block :to="friend_route(i.id)">
                                    詳しく
                                </v-btn>
                            </v-col>
                        </v-row>
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
        name: "stuff1",
        tags: [
            "学習支援",
            "英語",
            "高校受験"
        ]
    },
    {
        id: "stuff2",
        name: "stuff2",
        tags: [
            "学習支援",
            "英語",
            "高校受験"
        ]
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
  