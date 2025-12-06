const cells = document.querySelectorAll(".cell");
const statusText = document.getElementById("status");
const restartBtn = document.getElementById("restartBtn");

let board = ["", "", "", "", "", "", "", "", ""];
let human = "X";
let ai = "O";
let gameOver = false;

cells.forEach(cell => cell.addEventListener("click", handleHumanTurn));
restartBtn.addEventListener("click", restartGame);

function handleHumanTurn(e) {
    const index = e.target.dataset.index;

    if (board[index] !== "" || gameOver) return;

    board[index] = human;
    e.target.textContent = human;

    if (checkWinner(board, human)) {
        statusText.textContent = "You Win!";
        gameOver = true;
        return;
    }

    if (isBoardFull(board)) {
        statusText.textContent = "Draw!";
        gameOver = true;
        return;
    }

    statusText.textContent = "AI's Turn...";
    setTimeout(aiTurn, 300);
}

function aiTurn() {
    const bestMove = minimax(board, 0, -Infinity, Infinity, true).index;
    board[bestMove] = ai;
    cells[bestMove].textContent = ai;

    if (checkWinner(board, ai)) {
        statusText.textContent = "AI Wins!";
        gameOver = true;
        return;
    }

    if (isBoardFull(board)) {
        statusText.textContent = "Draw!";
        gameOver = true;
        return;
    }

    statusText.textContent = "Your Turn (X)";
}

function minimax(newBoard, depth, alpha, beta, maxPlayer) {
    if (checkWinner(newBoard, human)) return { score: -10 + depth };
    if (checkWinner(newBoard, ai)) return { score: 10 - depth };
    if (isBoardFull(newBoard)) return { score: 0 };

    let bestMove = maxPlayer ? { score: -Infinity } : { score: Infinity };

    for (let i = 0; i < 9; i++) {
        if (newBoard[i] === "") {
            newBoard[i] = maxPlayer ? ai : human;

            let result = minimax(newBoard, depth + 1, alpha, beta, !maxPlayer);
            result.index = i;

            newBoard[i] = "";

            if (maxPlayer) {
                if (result.score > bestMove.score) bestMove = result;
                alpha = Math.max(alpha, result.score);
            } else {
                if (result.score < bestMove.score) bestMove = result;
                beta = Math.min(beta, result.score);
            }

            if (beta <= alpha) break;
        }
    }

    return bestMove;
}

function checkWinner(b, player) {
    const wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ];

    return wins.some(c => c.every(i => b[i] === player));
}

function isBoardFull(b) {
    return b.every(cell => cell !== "");
}

function restartGame() {
    board = ["", "", "", "", "", "", "", "", ""];
    gameOver = false;
    cells.forEach(cell => cell.textContent = "");
    statusText.textContent = "Your turn (X)";
}
