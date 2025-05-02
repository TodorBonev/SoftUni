function ticTacToe(moves) {
    const board = [
      [false, false, false],
      [false, false, false],
      [false, false, false],
    ];
    
    function isBoardFull(board) {
      return board.every(row => row.every(cell => cell !== false));
    }
    
    function hasPlayerWon(board, Player) {

      for (let i = 0; i < 3; i++) {
        if (board[i][0] === Player && board[i][0] === board[i][1] && board[i][1] === board[i][2]) {
          return true;
        }
      }
      
      for (let i = 0; i < 3; i++) {
        if (board[0][i] === Player && board[0][i] === board[1][i] && board[1][i] === board[2][i]) {
          return true;
        }
      }
      
      if ((board[0][0] === Player && board[0][0] === board[1][1] && board[1][1] === board[2][2]) ||
          (board[0][2] === Player && board[0][2] === board[1][1] && board[1][1] === board[2][0])) {
        return true;
      }
      
      return false;
    }
    
    const players = ["X", "O"];
    let playerTurn = 0;
    let winner = null;
    
    for (const move of moves) {
      if (winner || isBoardFull(board)) {
        break;
      }
      
      const [row, col] = move.split(" ").map(Number);
      
      if (board[row][col] !== false) {
        console.log("This place is already taken. Please choose another!");
        continue;
      }
      
      const currentPlayer = players[playerTurn];
      board[row][col] = currentPlayer;
      
      if (hasPlayerWon(board, currentPlayer)) {
        winner = currentPlayer;
      }
      
      playerTurn = 1 - playerTurn;
    }
    
    if (winner) {
      console.log(`Player ${winner} wins!`);
    } else {
      console.log("The game ended! Nobody wins :(");
    }
    
    for (const row of board) {
      console.log(row.join("\t"));
    }
  }

