<script setup lang="ts">
import HelloWorld from "./components/HelloWorld.vue";
</script>

<template>
	<div class="board">
		<template v-for="i in 64" :key="i">
			<div class="cell">
				{{ i }}
			</div>
		</template>
	</div>
</template>

<style scoped></style>
