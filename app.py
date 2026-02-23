<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FlashDeal Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { background-color: #0f172a; color: white; font-family: sans-serif; }
        .glass-card { background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; }
        .sidebar { background-color: #1e293b; width: 260px; height: 100vh; }
        .gradient-text { background: linear-gradient(to right, #22d3ee, #0ea5e9); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .active-nav { background: rgba(255, 255, 255, 0.1); border-right: 4px solid #22d3ee; }
        .status-pulse { animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite; }
        @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: .5; } }
    </style>
</head>
<body class="flex">

    <aside class="sidebar p-4 flex flex-col gap-4 shadow-2xl">
        <div class="flex items-center gap-2 mb-6">
            <div class="w-3 h-3 rounded-full bg-green-500"></div>
            <div class="w-3 h-3 rounded-full bg-gray-600"></div>
        </div>
        
        <nav class="flex flex-col gap-1 text-gray-400">
            <div class="flex items-center gap-3 p-3 hover:bg-slate-700 rounded cursor-pointer">
                <i class="fas fa-th-large w-5"></i> FlashDeal-app
            </div>
            <div class="flex items-center gap-3 p-3 hover:bg-slate-700 rounded cursor-pointer">
                <i class="fas fa-users w-5"></i> FlashDeal-app
            </div>
            <div class="flex items-center gap-3 p-3 hover:bg-slate-700 rounded cursor-pointer">
                <i class="fas fa-phone-alt w-5"></i> Smart Control
            </div>
            <div class="flex items-center gap-3 p-3 hover:bg-slate-700 rounded cursor-pointer">
                <i class="fas fa-bars w-5"></i> App.py
            </div>
            <div class="flex items-center gap-3 p-3 hover:bg-slate-700 rounded cursor-pointer text-blue-400">
                <i class="fas fa-camera w-5"></i> 1011117
            </div>
            <div class="flex items-center gap-3 p-3 active-nav text-white cursor-pointer">
                <i class="fas fa-chevron-right w-5"></i> My FlashDeal Star
            </div>
            <div class="flex items-center gap-3 p-3 hover:bg-slate-700 rounded cursor-pointer">
                <i class="fas fa-microchip w-5"></i> 320.py
            </div>
            <div class="flex items-center gap-3 p-3 hover:bg-slate-700 rounded cursor-pointer">
                <i class="fas fa-cog w-5"></i> Settings
            </div>
            <div class="flex items-center gap-3 p-3 text-cyan-500 hover:bg-slate-700 rounded cursor-pointer">
                <i class="fas fa-lock w-5"></i> Secure_val.html
            </div>
        </nav>
    </aside>

    <main class="flex-1 p-8">
        <header class="flex justify-between items-start mb-10">
            <div>
                <h1 class="text-4xl font-bold flex items-center gap-2">
                    <i class="fas fa-bolt text-cyan-400"></i>
                    <span class="text-cyan-400">Flash</span>Deal
                </h1>
                <p class="text-gray-400 mt-2 text-xl italic">Talk. Pay. Done.</p>
            </div>
            <div class="text-right">
                <h1 class="text-3xl font-bold text-cyan-400 flex items-center gap-2 justify-end">
                    <i class="fas fa-bolt"></i> FlashDeal
                </h1>
            </div>
        </header>

        <div class="flex gap-4 mb-8">
            <button class="flex items-center gap-2 px-8 py-3 glass-card border-b-2 border-cyan-400">
                <i class="fas fa-microphone"></i> Voice Command
            </button>
            <button class="flex items-center gap-2 px-8 py-3 glass-card opacity-60">
                <i class="fas fa-coins"></i> Token Wallet
            </button>
            <button class="flex items-center gap-2 px-8 py-3 glass-card opacity-60">
                <i class="fas fa-shield-alt"></i> Security Star
            </button>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            
            <div class="glass-card p-6 relative overflow-hidden lg:col-span-2">
                <span class="absolute top-4 left-4 text-gray-500 text-sm font-mono">#42</span>
                <h3 class="text-xl font-semibold mb-6 ml-8">Smart Voice Command System</h3>
                <div class="flex justify-between items-center">
                    <div class="space-y-2">
                        <p class="text-xs text-gray-500 font-mono">https://media.flashdeal.io/v1/system/wave.gif</p>
                        <p class="text-cyan-400 italic text-lg status-pulse">Listening for your command...</p>
                        <p class="text-gray-300">"Send 50 Tokens"</p>
                    </div>
                    <div class="flex items-center gap-1">
                        <div class="flex gap-1 h-12 items-center">
                            <div class="w-1 bg-cyan-400 h-4"></div>
                            <div class="w-1 bg-cyan-400 h-8"></div>
                            <div class="w-1 bg-cyan-400 h-12"></div>
                            <div class="w-1 bg-cyan-400 h-6"></div>
                            <div class="w-1 bg-cyan-400 h-10"></div>
                        </div>
                        <span class="text-xs text-cyan-500 font-bold ml-2">GIF</span>
                    </div>
                </div>
            </div>

            <div class="glass-card p-6 relative">
                <span class="absolute top-4 left-4 text-gray-500 text-sm font-mono">#43</span>
                <h3 class="text-xl font-semibold mb-8 ml-8">FlashDeal Token Wallet</h3>
                <div class="grid grid-cols-2 gap-4 text-center border-b border-gray-700 pb-6">
                    <div>
                        <p class="text-gray-400 text-sm mb-1">Current Balance</p>
                        <p class="text-2xl font-bold">1,250 FTK</p>
                        <p class="text-xs text-green-500 mt-2">● Synced</p>
                    </div>
                    <div class="border-l border-gray-700">
                        <p class="text-gray-400 text-sm mb-1">Last Transaction</p>
                        <p class="text-2xl font-bold text-red-400">-50 FTK</p>
                        <p class="text-xs text-gray-500 mt-2">● Inverse</p>
                    </div>
                </div>
                <div class="mt-6">
                    <p class="text-sm text-gray-400 mb-4 italic">Recent Activity: Safe & Encrypted</p>
                    <div class="flex items-center justify-between">
                        <button class="bg-cyan-400 text-black font-bold py-2 px-6 rounded-md hover:bg-cyan-300 transition">
                            Activate Button
                        </button>
                        <div class="flex items-center gap-2">
                            <span class="text-xs text-gray-500">Transform: 3.00.1.20</span>
                            <i class="fas fa-ellipsis-h text-gray-500"></i>
                        </div>
                    </div>
                </div>
            </div>

            <div class="glass-card p-6 relative">
                <span class="absolute top-4 left-4 text-gray-500 text-sm font-mono">#2</span>
                <h3 class="text-xl font-semibold mb-6 ml-8">My FlashDeal Star Protection</h3>
                <div class="space-y-4">
                    <div class="flex items-center gap-2 text-gray-300 mb-4">
                        <i class="fas fa-chevron-circle-down"></i>
                        <span class="font-bold">Settings</span>
                    </div>
                    <hr class="border-gray-700 mb-6">
                    <div class="space-y-3">
                        <label class="flex items-center gap-3 cursor-pointer">
                            <input type="checkbox" checked class="accent-cyan-400">
                            <span class="text-sm">Face ID Verification</span>
                            <span class="text-[10px] bg-gray-700 px-1 rounded text-gray-400">ID</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer">
                            <input type="checkbox" class="accent-cyan-400">
                            <span class="text-sm">Mutual Token Protocol</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer">
                            <input type="checkbox" class="accent-cyan-400">
                            <span class="text-sm">Control Protocol</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer">
                            <input type="checkbox" class="accent-cyan-400">
                            <span class="text-sm">Body Movement Compatibility</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer">
                            <input type="checkbox" class="accent-cyan-400">
                            <span class="text-sm">Offline Mode (False)</span>
                        </label>
                    </div>
                    <div class="h-1 bg-cyan-900 mt-6 rounded-full">
                        <div class="h-full bg-cyan-400 w-2/3 shadow-[0_0_10px_#22d3ee]"></div>
                    </div>
                </div>
            </div>

            <div class="lg:col-span-2 mt-4">
                <button class="bg-gradient-to-r from-purple-500 to-cyan-400 text-black font-bold py-2 px-8 rounded-md mb-6 shadow-lg">
                    Commit changes
                </button>
                <div class="glass-card p-6 flex justify-between items-end">
                    <div>
                        <div class="flex items-center gap-2 text-gray-400 mb-4">
                            <i class="fas fa-code"></i>
                            <span class="font-mono">&lt;32 Settings&gt;</span>
                        </div>
                        <p class="text-sm text-gray-300">User: <span class="text-cyan-400 font-bold">Hannibal85090</span></p>
                        <p class="text-xs text-gray-500 mt-1 flex items-center gap-2">
                            <i class="fas fa-link text-green-500"></i> FlashDeal Star Device: Connected
                        </p>
                    </div>
                    <div class="flex items-center gap-4">
                        <i class="fas fa-ellipsis-h text-gray-600 text-2xl"></i>
                        <i class="fas fa-star text-gray-400 text-4xl opacity-50"></i>
                    </div>
                </div>
            </div>
        </div>
    </main>
</body>
</html>
