def isValidChessBoard(board):
    valid_positions = [f"{r}{c}" for r in "12345678" for c in "abcdefgh"]
    valid_pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

    piece_counts = {}
    player_piece_counts = {'w': 0, 'b': 0}
    pawn_counts = {'w': 0, 'b': 0}
    king_counts = {'w': 0, 'b': 0}

    for position, piece in board.items():
        # Check position validity
        if position not in valid_positions:
            return False

        # Check piece format
        if len(piece) < 2 or piece[0] not in ['w', 'b'] or piece[1:] not in valid_pieces:
            return False

        colour = piece[0]
        kind = piece[1:]

        # Count per piece
        piece_counts[piece] = piece_counts.get(piece, 0) + 1
        player_piece_counts[colour] += 1
        if kind == 'pawn':
            pawn_counts[colour] += 1
        if kind == 'king':
            king_counts[colour] += 1

    # Final validity checks
    if king_counts['w'] != 1 or king_counts['b'] != 1:
        return False
    if pawn_counts['w'] > 8 or pawn_counts['b'] > 8:
        return False
    if player_piece_counts['w'] > 16 or player_piece_counts['b'] > 16:
        return False

    return True

chessBoard = {
    '1a': 'wrook', '1b': 'wknight', '1c': 'wbishop', '1d': 'wqueen', '1e': 'wking',
    '1f': 'wbishop', '1g': 'wknight', '1h': 'wrook',
    '2a': 'wpawn', '2b': 'wpawn', '2c': 'wpawn', '2e': 'wpawn', '2f': 'wpawn', '2g': 'wpawn', '2h': 'wpawn',
    '7a': 'bpawn', '7b': 'bpawn', '7c': 'bpawn', '7e': 'bpawn', '7f': 'bpawn', '7g': 'bpawn', '7h': 'bpawn',
    '8a': 'brook', '8b': 'bknight', '8c': 'bbishop', '8d': 'bqueen', '8e': 'bking', '8f': 'bbishop', '8g': 'bknight', '8h': 'brook'
}

print(isValidChessBoard(chessBoard))  