<template>
    <Timeline :value="events" align="alternate" class="customized-timeline">
        <template #marker="slotProps">
			<span class="custom-marker p-shadow-2" :style="{backgroundColor: slotProps.item.color}">
				<i :class="slotProps.item.icon"></i>
			</span>
        </template>
        <template #content="slotProps">
            <Card>
                <template #title>
                    {{slotProps.item.status}}
                </template>
                <template #subtitle>
                    {{slotProps.item.date}}
                </template>
                <template #content>
                    <img v-if="slotProps.item.image" :src="'demo/images/product/' + slotProps.item.image" :alt="slotProps.item.name" width="200" class="p-shadow-2" />
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt
                        quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque quas!</p>
                    <Button label="Read more" class="p-button-text"></Button>
                </template>
            </Card>
        </template>
    </Timeline>
</template>

<script>
    export default {
        name: "ActivityLog",
        props: [ "events" ]
    }
</script>

<style scoped>

</style>
