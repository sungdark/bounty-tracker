const bounties = require('./bounties.json');
const pendingPayment = bounties.filter(b => b.status === 'pending_payment').reduce((sum, b) => sum + (b.reward_value || 0), 0);
const inProgress = bounties.filter(b => b.status === 'in_progress').length;
const completed = bounties.filter(b => b.status === 'completed').reduce((sum, b) => sum + (b.reward_value || 0), 0);
const highValue = bounties.filter(b => b.reward_value >= 0.5).slice(0, 2).map(b => `${b.notes} ($${b.reward_value.toFixed(2)})`);
console.log(JSON.stringify({ pendingPayment, inProgress, completed, highValue }));
