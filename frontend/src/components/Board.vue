<script setup lang="ts">
import Piece from "./Piece.vue";

interface Piece {
	type: string | null;
	color: string | null;
	row: number;
	col: string;
}

const COLUMNS: string[] = ["a", "b", "c", "d", "e", "f", "g", "h"];

const generateMajorPiecesRow = (color: string, row: number): Piece[] => [
	{ type: "rook", color, row, col: "a" },
	{ type: "knight", color, row, col: "b" },
	{ type: "bishop", color, row, col: "c" },
	{ type: "queen", color, row, col: "d" },
	{ type: "king", color, row, col: "e" },
	{ type: "bishop", color, row, col: "f" },
	{ type: "knight", color, row, col: "g" },
	{ type: "rook", color, row, col: "h" },
];

const generatePawnRow = (color: string, row: number): Piece[] =>
	COLUMNS.map((col: string) => ({ type: "pawn", color, row, col }));

const generateEmptyRow = (row: number): Piece[] =>
	COLUMNS.map((col: string) => ({ type: null, color: null, row, col }));

const initialBoard: Piece[][] = [
	generateMajorPiecesRow("black", 1),
	generatePawnRow("black", 2),

	generateEmptyRow(3),
	generateEmptyRow(4),
	generateEmptyRow(5),
	generateEmptyRow(6),

	generatePawnRow("white", 7),
	generateMajorPiecesRow("white", 8),
];
</script>

<template>
	<div class="board">
		<div
			v-for="(row, rowIndex) in initialBoard"
			:key="rowIndex"
			class="board__row"
		>
			<template v-for="(col, _) in row" :key="`${col.row}-${col.col}`">
				<Piece
					:row="col?.row"
					:col="col?.col"
					:color="col?.color"
					:type="col?.type"
				/>
			</template>
		</div>
	</div>
</template>

<style scoped>
.board {
	grid-area: center;

	display: flex;
	flex-direction: column;
	width: var(--board-size);
	height: var(--board-size);

	background: conic-gradient(
		var(--color-even) 90deg,
		var(--color-odd) 90deg 180deg,
		var(--color-even) 180deg 270deg,
		var(--color-odd) 270deg
	);
	background-size: calc(var(--cell-size) * 2) calc(var(--cell-size) * 2);
}

.board__row {
	display: flex;
}
</style>
