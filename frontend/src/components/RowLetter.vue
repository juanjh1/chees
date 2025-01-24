<script setup lang="ts">
type Position = "TOP" | "BOTTOM";

defineProps<{ position: Position }>();

const letters: string[] = ["", "A", "B", "C", "D", "E", "F", "G", "H", ""];
</script>

<template>
	<div class="row" :class="position.toLowerCase()">
		<template v-for="letter in letters" :key="letter">
			<div class="letter" :class="letter === '' ? 'empty-cell' : ''">
				{{ letter }}
			</div>
		</template>
	</div>
</template>

<style scoped>
.top {
	grid-area: top;
}

.bottom {
	grid-area: bottom;
}

.row {
	display: flex;
	justify-content: space-between;
	width: calc(var(--board-size) + var(--cell-size));
	height: calc(var(--cell-size) / 2);
}

.letter {
	display: inline-flex;
	justify-content: center;
	align-items: center;
	text-align: center;
	color: var(--white-secondary);
}

.letter {
	width: var(--cell-size);
	height: calc(var(--cell-size) / 2);
}

.empty-cell {
	width: calc(var(--cell-size) / 2);
	height: calc(var(--cell-size) / 2);
}
</style>
