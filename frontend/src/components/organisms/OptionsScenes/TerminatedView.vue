<template>
    <div class="flex flex-wrap w-full justify-center items-center">

        <header class="w-full mx-16">
            <div class="w-full flex justify-between items-center">
                <div>
                    <h1 class="text-2xl">Session terminated</h1>
                    <h2 class="text-lg text-opacity-25">Activity summary:</h2>
                </div>
                <div class="text-lg">
                    {{ new Date().getHours() < 10 ? `0${new Date().getHours()}` : `${new Date().getHours()}`}}:{{ new Date().getMinutes() < 10 ? `0${new Date().getMinutes()}` : `${new Date().getMinutes()}`}} | 28.03.2020r.
                </div>
            </div>
            <hr class="w-full my-4"/>
        </header>

        <div class="flex justify-center flex-wrap w-full">

            <Card style="position: relative; width: 40vw; margin: 1.5rem">
                <template #title>
                    Confirmed activities:
                </template>
                <template #content>
                    <Chart type="bar" :data="stackedData" :options="stackedOptions" v-if="!loading1" />
                    <ProgressSpinner class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2" v-if="loading1" />
                </template>
            </Card>

            <Card style="position: relative; width: 20vw; margin: 1.5rem">
                <template #title>
                    Participants list:
                </template>
                <template #content>
                    <ul v-for="user of users" v-if="!loading2">
                        <li class="flex items-center p-3">
                            <Avatar :label="user.charAt(0).toUpperCase()" class="mr-2" />
                            <p>{{ user }}</p>
                        </li>
                    </ul>
                    <ProgressSpinner  class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2" v-if="loading2" />
                </template>
            </Card>

            <Card style="position: relative; width: 26vw; margin: 1.5rem">
                <template #title>
                    Questions and answers:
                </template>
                <template #content>
                    <QuestionsLog :questions="questions" :is-end-screen="true" />
                    <ProgressSpinner class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2" v-if="loading2" />
                </template>
            </Card>

        </div>

    </div>
</template>

<script>
    import Chart from 'primevue/chart';
    import Card from 'primevue/card';
    import ProgressSpinner from 'primevue/progressspinner';
    import QuestionsLog from './QuestionsLog';
    import Avatar from 'primevue/avatar';

    export default {
        name: "TerminatedView",
        props: [ "questions", "users" ],
        components: {
            QuestionsLog,
            Chart,
            Card,
            ProgressSpinner,
            Avatar
        },
        data(){
            return {
                loading1: true,
                loading2: true,
                stackedData: {
                    labels: [],
                    datasets: [
                        {
                            type: 'bar',
                            label: 'Missed activity',
                            backgroundColor: '#cf1f1f',
                            data: []
                        },
                        {
                            type: 'bar',
                            label: 'Confirmed activity',
                            backgroundColor: '#51a753',
                            data: []
                        }
                    ]
                },
                stackedOptions: {
                    tooltips: {
                        mode: 'index',
                        intersect: false
                    },
                    responsive: true,
                    scales: {
                        xAxes: [{
                            stacked: true,
                        }],
                        yAxes: [{
                            stacked: true
                        }]
                    }
                }
            }
        },
        mounted() {

            function getRandomInt(min, max) {
                min = Math.ceil(min);
                max = Math.floor(max);
                return Math.floor(Math.random() * (max - min)) + min;
            }

            const firstTimeout = getRandomInt(2,3), secondTimeout = getRandomInt(3,5);

            setTimeout(()=>{
                this.stackedData.labels = [
                    "Benedykt K.",
                    "Paweł P.",
                    "Filip D.",
                    "Jędrzej Sz.",
                    "Paweł B."
                ];
                // Missed activities
                this.stackedData.datasets[0].data = [ 6, 1, 2, 1, 5 ];
                // Confirmed activities
                this.stackedData.datasets[1].data = [ 0, 5, 4, 5, 1 ];
                this.loading1 = false;
            }, firstTimeout);
            setTimeout(()=>{
                this.loading2 = false;
            }, secondTimeout);
        }
    }
</script>

<style scoped>

</style>
