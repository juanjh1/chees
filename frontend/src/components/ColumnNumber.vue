<script setup lang="ts">
type Position = "RIGHT" | "LEFT";
defineProps<{ position: Position }>();

const numbers: string[] = ["1", "2", "3", "4", "5", "6", "7", "8"];
</script>

<template>
	<div class="column" :class="position.toLowerCase()">
		<template v-for="number in numbers" :key="number">
			<div class="number">{{ number }}</div>
		</template>
	</div>
</template>

<style scoped>
.left {
	grid-area: left;
}

.right {
	grid-area: right;
}

.column {
	display: flex;
	flex-direction: column;
	justify-content: space-around;
	width: calc(var(--cell-size) / 2);
	height: var(--board-size);
}

.number {
	display: inline-flex;
	justify-content: center;
	align-items: center;
	text-align: center;
	color: var(--white-secondary);
}
</style>
