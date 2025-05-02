function result(command) {
    if (command === 'upvote') return this.upvotes++;
    if (command === 'downvote') return this.downvotes++;

    const [upvote, downvote] = [this.upvotes, this.downvotes];
    const totalVotes = upvote + downvote, balance = upvote - downvote;

    const ratingState = () =>
        totalVotes < 10 ? 'new' :
        upvote > totalVotes * 0.66 ? 'hot' :
        balance >= 0 && totalVotes > 100 ? 'controversial' :
        balance < 0 ? 'unpopular' : 'new';

    const inflateVote = totalVotes > 50 ? Math.ceil(Math.max(upvote, downvote) * 0.25) : 0;
    
    return [upvote + inflateVote, downvote + inflateVote, balance, ratingState()];
}

