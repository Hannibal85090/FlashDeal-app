<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { background-color: #020617; color: #f8fafc; font-family: 'Inter', sans-serif; overflow-x: hidden; }
        .slide-card { background: linear-gradient(145deg, #0f172a 0%, #1e293b 100%); border: 1px solid rgba(34, 211, 238, 0.2); border-radius: 1.5rem; transition: transform 0.3s ease; }
        .slide-card:hover { transform: translateY(-5px); border-color: #22d3ee; }
        .neon-glow { text-shadow: 0 0 15px rgba(34, 211, 238, 0.6); }
        .gradient-text { background: linear-gradient(to right, #22d3ee, #3b82f6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        canvas { max-height: 200px !important; }
    </style>
</head>
<body class="p-6 md:p-12">

    <header class="text-center mb-16">
        <div class="inline-block p-2 px-6 bg-cyan-950/30 border border-cyan-500/30 rounded-full mb-4">
            <span class="text-cyan-400 text-sm tracking-widest uppercase font-bold">Investor Presentation 2026</span>
        </div>
        <h1 class="text-5xl md:text-7xl font-black mb-4 neon-glow uppercase">The Future of Transactions</h1>
        <p class="text-xl text-gray-400">FlashDeal: <span class="italic font-light">Talk. Pay. Done.</span></p>
    </header>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
        
        <div class="slide-card p-8 flex flex-col items-center text-center">
            <div class="w-16 h-16 bg-cyan-500/10 rounded-full flex items-center justify-center mb-6">
                <i class="fas fa-bolt text-3xl text-cyan-400"></i>
            </div>
            <h3 class="text-2xl font-bold mb-4">Speed & Execution</h3>
            <p class="text-gray-400 text-sm leading-relaxed">
                Execute payments in seconds using only your voice. No cards, no typing, just seamless flow.
            </p>
        </div>

        <div class="slide-card p-8 flex flex-col items-center text-center border-cyan-500/50 shadow-lg shadow-cyan-500/10">
            <div class="w-16 h-16 bg-blue-500/10 rounded-full flex items-center justify-center mb-6">
                <i class="fas fa-shield-halved text-3xl text-blue-400"></i>
            </div>
            <h3 class="text-2xl font-bold mb-4">Security Star</h3>
            <p class="text-gray-400 text-sm leading-relaxed">
                Biometric encryption, Mutual Token Protocol, and facial recognition ensuring every "Deal" is 100% secure.
            </p>
        </div>

        <div class="slide-card p-8 flex flex-col items-center text-center">
            <div class="w-16 h-16 bg-purple-500/10 rounded-full flex items-center justify-center mb-6">
                <i class="fas fa-brain text-3xl text-purple-400"></i>
            </div>
            <h3 class="text-2xl font-bold mb-4">AI-Driven Insights</h3>
            <p class="text-gray-400 text-sm leading-relaxed">
                A simplified ecosystem connecting AI that learns user habits to optimize spending and security.
            </p>
        </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        
        <div class="slide-card p-8">
            <div class="flex justify-between items-center mb-8">
                <h3 class="text-xl font-bold"><i class="fas fa-chart-line mr-2 text-cyan-400"></i> Projected Market Growth</h3>
                <span class="text-xs text-gray-500">2024 - 2027</span>
            </div>
            <canvas id="growthChart"></canvas>
        </div>

        <div class="slide-card p-8 bg-slate-900">
            <h3 class="text-xl font-bold mb-6"><i class="fas fa-eye mr-2 text-blue-400"></i> Future Vision & Scaling</h3>
            <div class="space-y-6">
                <div class="flex items-center gap-4">
                    <span class="text-3xl font-bold text-cyan-400">75%</span>
                    <div class="flex-1">
                        <p class="text-sm font-semibold">User Adoption Growth</p>
                        <div class="w-full bg-gray-700 h-1.5 rounded-full mt-1">
                            <div class="bg-cyan-400 h-1.5 rounded-full" style="width: 75%"></div>
                        </div>
                    </div>
                </div>
                <div class="flex items-center gap-4">
                    <span class="text-3xl font-bold text-purple-400">99.9%</span>
                    <div class="flex-1">
                        <p class="text-sm font-semibold">Security Reliability</p>
                        <div class="w-full bg-gray-700 h-1.5 rounded-full mt-1">
                            <div class="bg-purple-400 h-1.5 rounded-full" style="width: 99%"></div>
                        </div>
                    </div>
                </div>
                <p class="text-gray-500 text-xs italic mt-4">
                    * Scaling focus: Expanding "My FlashDeal Star" hardware integration and telecom partnerships.
                </p>
            </div>
        </div>
    </div>

    <footer class="mt-16 text-center border-t border-gray-800 pt-12">
        <h2 class="text-3xl font-bold mb-8 italic">Join the Future of Finance</h2>
        <div class="flex flex-wrap justify-center gap-4">
            <button class="bg-cyan-500 hover:bg-cyan-400 text-black px-10 py-4 rounded-xl font-black transition shadow-lg shadow-cyan-500/20">
                REQUEST DEMO
            </button>
            <button class="border border-white/20 hover:bg-white/5 px-10 py-4 rounded-xl font-bold transition">
                INVESTOR RELATIONS
            </button>
        </div>
        <p class="mt-8 text-gray-600 text-sm tracking-widest">FLASHDEAL © 2026 | THE REVOLUTION IS AUDIBLE</p>
    </footer>

    <script>
        const ctx = document.getElementById('growthChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['2024', '2025', '2026', '2027'],
                datasets: [{
                    label: 'Projected Revenue (Millions)',
                    data: [12, 45, 110, 280],
                    borderColor: '#22d3ee',
                    backgroundColor: 'rgba(34, 211, 238, 0.1)',
                    fill: true,
                    tension: 0.4,
                    borderWidth: 3,
                    pointBackgroundColor: '#fff'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false } },
                scales: {
                    y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#64748b' } },
                    x: { grid: { display: false }, ticks: { color: '#64748b' } }
                }
            }
        });
    </script>
</body>
</html>
