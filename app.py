<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root { --neon-cyan: #22d3ee; --deep-space: #020617; }
        body { background-color: var(--deep-space); color: white; font-family: 'Inter', sans-serif; }
        .star-gradient { background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); border: 1px solid rgba(34, 211, 238, 0.3); }
        .token-glow { box-shadow: 0 0 20px rgba(34, 211, 238, 0.2); }
    </style>
</head>
<body class="p-4 md:p-10">
    <div class="max-w-6xl mx-auto">
        <div class="flex justify-between items-center border-b border-gray-800 pb-6 mb-10">
            <div>
                <h1 class="text-4xl font-black tracking-tighter text-cyan-400">FlashDeal</h1>
                <p class="text-gray-500 italic">Talk. Pay. Done.</p>
            </div>
            <div class="text-right">
                <div class="text-xs uppercase tracking-widest text-gray-400 mb-1">Security Status</div>
                <div class="flex items-center gap-2 text-green-400">
                    <span class="relative flex h-3 w-3"><span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span><span class="relative inline-flex rounded-full h-3 w-3 bg-green-500"></span></span>
                    My FlashDeal Star Connected
                </div>
            </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <div class="lg:col-span-1 space-y-6">
                <div class="star-gradient p-6 rounded-2xl token-glow">
                    <h3 class="text-cyan-400 font-bold mb-4 uppercase text-sm tracking-widest">Token Wallet</h3>
                    <div class="text-3xl font-mono mb-2">1,250.00 FTK</div>
                    <div class="text-xs text-gray-500">Mutual Token Protocol Active</div>
                </div>

                <div class="star-gradient p-6 rounded-2xl">
                    <h3 class="text-gray-300 font-bold mb-4 flex items-center gap-2">
                        <i class="fas fa-fingerprint text-cyan-400"></i> Biometric Security
                    </h3>
                    <ul class="space-y-3 text-sm">
                        <li class="flex justify-between"><span>Face ID</span> <i class="fas fa-check text-cyan-500"></i></li>
                        <li class="flex justify-between"><span>Body Movement</span> <i class="fas fa-check text-cyan-500"></i></li>
                        <li class="flex justify-between text-gray-500"><span>Mutual Token</span> <span>Active</span></li>
                    </ul>
                </div>
            </div>

            <div class="lg:col-span-2 star-gradient p-8 rounded-2xl relative overflow-hidden">
                <div class="relative z-10">
                    <h2 class="text-3xl font-bold mb-6">Future Vision: Scaling 2026</h2>
                    <p class="text-gray-400 leading-relaxed mb-8">
                        Our parallel project focuses on <span class="text-white font-bold">Hardware Integration</span>. 
                        We are building a lightweight device—The FlashDeal Star—to revolutionize car and home access via voice tokens.
                    </p>
                    <div class="grid grid-cols-2 gap-4">
                        <div class="bg-black/40 p-4 rounded-xl">
                            <div class="text-2xl font-bold text-cyan-400">+320%</div>
                            <div class="text-xs text-gray-500 uppercase">Growth Projection</div>
                        </div>
                        <div class="bg-black/40 p-4 rounded-xl">
                            <div class="text-2xl font-bold text-cyan-400">Zero</div>
                            <div class="text-xs text-gray-500 uppercase">Fraud Incidents</div>
                        </div>
                    </div>
                </div>
                <div class="absolute -bottom-10 -right-10 w-64 h-64 bg-cyan-500/10 rounded-full blur-3xl"></div>
            </div>
        </div>

        <div class="mt-12 flex justify-center gap-6">
            <button class="bg-cyan-500 text-black px-8 py-3 rounded-full font-bold hover:bg-cyan-400 transition">Request Demo</button>
            <button class="border border-gray-700 px-8 py-3 rounded-full font-bold hover:bg-white/5 transition">Investor Pitch PDF</button>
        </div>
    </div>
</body>
</html>
