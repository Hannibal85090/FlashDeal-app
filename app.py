<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { background-color: #0f172a; color: #f8fafc; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        .glass-card { background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 1rem; }
        .neon-text { color: #22d3ee; text-shadow: 0 0 10px rgba(34, 211, 238, 0.5); }
        .neon-border { border-bottom: 2px solid #22d3ee; }
        .waveform { display: flex; align-items: center; gap: 3px; height: 40px; }
        .bar { width: 4px; background: #22d3ee; border-radius: 2px; animation: pulse 1.2s infinite ease-in-out; }
        @keyframes pulse { 0%, 100% { height: 10px; } 50% { height: 40px; } }
    </style>
</head>
<body class="p-4 md:p-8">

    <header class="flex justify-between items-center mb-8">
        <div>
            <div class="flex items-center gap-2">
                <i class="fas fa-bolt text-3xl neon-text"></i>
                <h1 class="text-4xl font-bold tracking-wider">FlashDeal</h1>
            </div>
            <p class="text-gray-400 mt-1 italic">Talk. Pay. Done.</p>
        </div>
        <div class="text-right">
            <span class="bg-cyan-900/50 text-cyan-300 px-3 py-1 rounded-full text-sm border border-cyan-700">
                <i class="fas fa-link mr-2"></i>My FlashDeal Star: Connected
            </span>
        </div>
    </header>

    <div class="flex gap-4 mb-6 border-b border-gray-700">
        <button class="pb-2 neon-border px-4 flex items-center gap-2"><i class="fas fa-microphone"></i> Voice Command</button>
        <button class="pb-2 text-gray-500 px-4 flex items-center gap-2 hover:text-white"><i class="fas fa-wallet"></i> Token Wallet</button>
        <button class="pb-2 text-gray-500 px-4 flex items-center gap-2 hover:text-white"><i class="fas fa-star"></i> Security Star</button>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        
        <div class="glass-card p-6">
            <div class="flex justify-between items-start mb-4">
                <h2 class="text-xl font-semibold">#42 Smart Voice Command</h2>
                <span class="text-xs text-cyan-400 bg-cyan-950 px-2 py-1 rounded">LIVE</span>
            </div>
            <div class="flex items-center justify-between bg-slate-900/50 p-6 rounded-lg">
                <div>
                    <p class="text-gray-400 mb-2">Listening for your command...</p>
                    <p class="text-xl font-mono">"Send 50 Tokens"</p>
                </div>
                <div class="waveform">
                    <div class="bar" style="animation-delay: 0.1s"></div>
                    <div class="bar" style="animation-delay: 0.3s"></div>
                    <div class="bar" style="animation-delay: 0.2s"></div>
                    <div class="bar" style="animation-delay: 0.5s"></div>
                    <div class="bar" style="animation-delay: 0.4s"></div>
                </div>
            </div>
        </div>

        <div class="glass-card p-6 row-span-2">
            <h2 class="text-xl font-semibold mb-4 flex items-center gap-2">
                <i class="fas fa-shield-halved text-cyan-400"></i> #2 My FlashDeal Star Protection
            </h2>
            <div class="space-y-4 mt-6">
                <div class="flex items-center justify-between p-3 bg-slate-800/30 rounded">
                    <label class="flex items-center gap-3">
                        <input type="checkbox" checked class="w-4 h-4 accent-cyan-500">
                        <span>Face ID Verification</span>
                    </label>
                    <i class="fas fa-check-circle text-green-500"></i>
                </div>
                <div class="flex items-center justify-between p-3 bg-slate-800/30 rounded">
                    <label class="flex items-center gap-3">
                        <input type="checkbox" checked class="w-4 h-4 accent-cyan-500">
                        <span>Mutual Token Protocol</span>
                    </label>
                    <i class="fas fa-shield text-cyan-500"></i>
                </div>
                <div class="flex items-center justify-between p-3 bg-slate-800/30 rounded">
                    <label class="flex items-center gap-3">
                        <input type="checkbox" class="w-4 h-4 accent-cyan-500">
                        <span>Body Movement Compatibility</span>
                    </label>
                </div>
                <div class="flex items-center justify-between p-3 bg-slate-800/30 rounded">
                    <label class="flex items-center gap-3">
                        <input type="checkbox" class="w-4 h-4 accent-cyan-500">
                        <span>Biometric Fingerprint</span>
                    </label>
                </div>
            </div>
            <button class="w-full mt-8 bg-gradient-to-r from-cyan-600 to-blue-600 py-3 rounded-lg font-bold hover:opacity-90 transition">
                Commit Security Changes
            </button>
        </div>

        <div class="glass-card p-6">
            <h2 class="text-xl font-semibold mb-4 italic">#43 FlashDeal Token Wallet</h2>
            <div class="grid grid-cols-2 gap-4 mb-6 text-center">
                <div class="border-r border-gray-700">
                    <p class="text-gray-400 text-sm">Current Balance</p>
                    <p class="text-2xl font-bold">1,250 <span class="text-cyan-400 text-sm">FTK</span></p>
                </div>
                <div>
                    <p class="text-gray-400 text-sm">Last Transaction</p>
                    <p class="text-2xl font-bold text-red-400">-50 <span class="text-sm">FTK</span></p>
                </div>
            </div>
            <div class="bg-black/20 p-3 rounded text-xs">
                <p class="text-green-400 font-mono italic text-center">Status: Safe & Encrypted (Token Active)</p>
            </div>
        </div>

    </div>

    <footer class="mt-8 flex justify-between items-center text-gray-500 text-sm">
        <div>User ID: Hanniball85090</div>
        <div class="flex gap-4">
            <span>v3.00.2.20</span>
            <span class="text-cyan-400 cursor-pointer underline">Terms of Security</span>
        </div>
    </footer>

</body>
</html>
