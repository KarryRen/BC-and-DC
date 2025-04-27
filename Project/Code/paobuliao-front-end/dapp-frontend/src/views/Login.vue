<!-- The exported code uses Tailwind CSS. Install Tailwind CSS in your dev environment to ensure all styles work. -->
<template>
<div class="min-h-screen bg-gray-50">
<!-- Header -->
<header class="bg-white shadow-md">
<div class="container mx-auto px-6 py-4 flex justify-between items-center">
<div v-if="activeTab !== 'registration'" class="flex items-center space-x-6">
<button
v-for="menu in navigationMenu"
:key="menu.id"
@click="changeTab(menu.id)"
:class="[
'px-4 py-2 text-sm font-medium rounded-md cursor-pointer whitespace-nowrap !rounded-button',
activeTab === menu.id ? 'bg-blue-600 text-white' : 'bg-transparent text-gray-600 hover:bg-gray-100'
]"
>
<i :class="[menu.icon, 'mr-2']"></i>
{{ menu.name }}
</button>
</div>
<div class="flex items-center">
<h1 class="text-2xl font-bold text-blue-600">Paobuliao</h1>
<span class="ml-2 text-gray-500 text-sm">DeFi Smart Contract Platform</span>
</div>
<div class="flex items-center space-x-6">
<div class="flex items-center space-x-4">
<div class="bg-blue-50 px-4 py-2 rounded-md">
<span class="text-sm text-gray-600">Balance:</span>
<span class="ml-1 font-bold text-gray-800">$2,450.00</span>
</div>
<div class="bg-green-50 px-4 py-2 rounded-md">
<span class="text-sm text-gray-600">Credit Score:</span>
<span class="ml-1 font-bold text-green-600">850</span>
<i class="fas fa-arrow-up text-green-600 ml-1 text-xs"></i>
</div>
<button class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 cursor-pointer whitespace-nowrap !rounded-button">
<i class="fas fa-user-circle mr-2"></i>
My Account
</button>
</div>
</div>
</div>
</header>
<!-- Main Content -->
<main class="container mx-auto px-6 py-8">
<!-- Hero Section -->
<div class="relative bg-gradient-to-r from-blue-50 to-white mb-16 rounded-xl overflow-hidden">
<div class="container mx-auto px-6 py-16 flex items-center">
<div class="w-1/2 pr-12">
<h1 class="text-5xl font-bold text-gray-900 mb-6">Secure Prepayments with Blockchain Technology</h1>
<p class="text-xl text-gray-600 mb-8">Paobuliao DApp prevents default on prepaid services using smart contracts for education, fitness, automotive services and more.</p>
<div class="flex space-x-4">
<button class="px-8 py-3 bg-blue-600 text-white font-medium rounded-md shadow-lg hover:bg-blue-700 cursor-pointer whitespace-nowrap !rounded-button">
Get Started
</button>
<button class="px-8 py-3 bg-white text-blue-600 font-medium rounded-md shadow-lg hover:bg-gray-50 cursor-pointer whitespace-nowrap !rounded-button">
Learn More
</button>
</div>
</div>
<div class="w-1/2">
<img src="https://readdy.ai/api/search-image?query=modern%20blockchain%20technology%20visualization%20with%20floating%20digital%20blocks%20and%20connections%2C%20futuristic%20design%20with%20blue%20gradient%20background%2C%20professional%203D%20rendering%2C%20clean%20and%20minimalist&width=600&height=400&seq=12&orientation=landscape"
alt="Blockchain Technology"
class="w-full h-auto rounded-lg shadow-2xl">
</div>
</div>
</div>
<!-- Features Section -->
<div class="container mx-auto px-6 mb-16">
<h2 class="text-3xl font-bold text-center text-gray-900 mb-12">Why Choose Paobuliao?</h2>
<div class="grid grid-cols-3 gap-8">
<div class="p-6 bg-white rounded-xl shadow-lg">
<div class="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center mb-4">
<i class="fas fa-shield-alt text-blue-600 text-xl"></i>
</div>
<h3 class="text-xl font-bold text-gray-800 mb-2">Secure Payments</h3>
<p class="text-gray-600">Smart contracts ensure your prepaid services are protected and funds are released only upon service delivery.</p>
</div>
<div class="p-6 bg-white rounded-xl shadow-lg">
<div class="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center mb-4">
<i class="fas fa-chart-line text-blue-600 text-xl"></i>
</div>
<h3 class="text-xl font-bold text-gray-800 mb-2">Transparent Tracking</h3>
<p class="text-gray-600">Monitor your service usage and payment progress in real-time through our blockchain-based platform.</p>
</div>
<div class="p-6 bg-white rounded-xl shadow-lg">
<div class="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center mb-4">
<i class="fas fa-handshake text-blue-600 text-xl"></i>
</div>
<h3 class="text-xl font-bold text-gray-800 mb-2">Trust & Reliability</h3>
<p class="text-gray-600">Build trust between service providers and customers with our automated contract enforcement system.</p>
</div>
</div>
</div>
<!-- Registration Screen -->
<div v-if="activeTab === 'registration'" class="bg-white rounded-lg shadow-lg p-8 mb-8">
<div class="flex justify-center mb-8">
<div class="relative inline-flex">
<button
@click="registrationType = 'user'"
:class="[
'px-6 py-3 text-sm font-medium rounded-l-full cursor-pointer whitespace-nowrap !rounded-button',
registrationType === 'user' ? 'bg-blue-600 text-white' : 'bg-gray-100 text-gray-700'
]"
>
<i class="fas fa-user mr-2"></i>
User
</button>
<button
@click="registrationType = 'merchant'"
:class="[
'px-6 py-3 text-sm font-medium rounded-r-full cursor-pointer whitespace-nowrap !rounded-button',
registrationType === 'merchant' ? 'bg-blue-600 text-white' : 'bg-gray-100 text-gray-700'
]"
>
<i class="fas fa-store mr-2"></i>
Merchant
</button>
</div>
</div>
<!-- User Registration Form -->
<div v-if="registrationType === 'user'" class="max-w-2xl mx-auto">
<h2 class="text-2xl font-bold text-gray-800 mb-6">User Registration</h2>
<div class="grid grid-cols-2 gap-6 mb-6">
<div>
<label class="block text-sm font-medium text-gray-700 mb-1">First Name</label>
<input type="text" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500" />
</div>
<div>
<label class="block text-sm font-medium text-gray-700 mb-1">Last Name</label>
<input type="text" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500" />
</div>
<div>
<label class="block text-sm font-medium text-gray-700 mb-1">Email Address</label>
<input type="email" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500" />
</div>
<div>
<label class="block text-sm font-medium text-gray-700 mb-1">Phone Number</label>
<input type="tel" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500" />
</div>
</div>
<div class="grid grid-cols-2 gap-6 mb-8">
<div class="border border-gray-200 rounded-lg p-4 flex flex-col items-center justify-center">
<div class="w-20 h-20 bg-blue-50 rounded-full flex items-center justify-center mb-4">
<i class="fas fa-fingerprint text-blue-600 text-3xl"></i>
</div>
<h3 class="font-medium text-gray-800 mb-2">Biometric Verification</h3>
<p class="text-sm text-gray-500 text-center mb-4">Upload your fingerprint or facial recognition data for secure authentication</p>
<button class="px-4 py-2 bg-blue-100 text-blue-600 rounded-md font-medium text-sm cursor-pointer whitespace-nowrap !rounded-button">
<i class="fas fa-upload mr-2"></i>
Upload Biometric Data
</button>
</div>
<div class="border border-gray-200 rounded-lg p-4 flex flex-col items-center justify-center">
<div class="w-20 h-20 bg-blue-50 rounded-full flex items-center justify-center mb-4">
<i class="fas fa-id-card text-blue-600 text-3xl"></i>
</div>
<h3 class="font-medium text-gray-800 mb-2">Document Verification</h3>
<p class="text-sm text-gray-500 text-center mb-4">Upload your ID card or passport for identity verification</p>
<button class="px-4 py-2 bg-blue-100 text-blue-600 rounded-md font-medium text-sm cursor-pointer whitespace-nowrap !rounded-button">
<i class="fas fa-upload mr-2"></i>
Upload Documents
</button>
</div>
</div>
<div class="flex justify-center">
<button
id="completeRegistrationBtn"
@click="handleRegistrationComplete"
class="px-8 py-3 bg-blue-600 text-white font-medium rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 cursor-pointer whitespace-nowrap !rounded-button">
Complete Registration
</button>
<!-- Confirmation Dialog -->
<div v-if="showConfirmDialog" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
<div class="bg-white rounded-lg p-8 max-w-md w-full mx-4">
<h3 class="text-xl font-bold text-gray-900 mb-4">Confirm Registration</h3>
<div class="mb-6">
<div class="grid grid-cols-2 gap-4 mb-4">
<div>
<p class="text-sm text-gray-500">First Name</p>
<p class="font-medium">{{ registrationData.firstName || 'Not provided' }}</p>
</div>
<div>
<p class="text-sm text-gray-500">Last Name</p>
<p class="font-medium">{{ registrationData.lastName || 'Not provided' }}</p>
</div>
<div>
<p class="text-sm text-gray-500">Email</p>
<p class="font-medium">{{ registrationData.email || 'Not provided' }}</p>
</div>
<div>
<p class="text-sm text-gray-500">Phone</p>
<p class="font-medium">{{ registrationData.phone || 'Not provided' }}</p>
</div>
</div>
<div class="text-sm text-gray-500 mb-2">Verification Status</div>
<div class="flex items-center space-x-2 mb-1">
<i class="fas" :class="registrationData.biometricData ? 'fa-check text-green-500' : 'fa-times text-red-500'"></i>
<span>Biometric Data</span>
</div>
<div class="flex items-center space-x-2">
<i class="fas" :class="registrationData.documentsUploaded ? 'fa-check text-green-500' : 'fa-times text-red-500'"></i>
<span>Documents Uploaded</span>
</div>
</div>
<div class="flex justify-end space-x-4">
<button
@click="handleEdit"
class="px-4 py-2 text-gray-700 bg-gray-100 rounded-md hover:bg-gray-200 font-medium cursor-pointer whitespace-nowrap !rounded-button">
Edit
</button>
<button
@click="handleConfirm"
class="px-4 py-2 text-white bg-blue-600 rounded-md hover:bg-blue-700 font-medium cursor-pointer whitespace-nowrap !rounded-button">
Confirm
</button>
</div>
</div>
</div>
<!-- Success Message -->
<div v-if="showSuccessMessage" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
<div class="bg-white rounded-lg p-8 max-w-md w-full mx-4 text-center">
<div class="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
<i class="fas fa-check text-green-500 text-2xl"></i>
</div>
<h3 class="text-xl font-bold text-gray-900 mb-2">Registration Successful!</h3>
<p class="text-gray-600 mb-4">Please check your email to complete the verification process.</p>
<div class="animate-spin h-8 w-8 border-4 border-blue-600 border-t-transparent rounded-full mx-auto"></div>
<p class="text-sm text-gray-500 mt-4">Redirecting to dashboard...</p>
</div>
</div>
</div>
</div>
<!-- Merchant Registration Form -->
<div v-if="registrationType === 'merchant'" class="max-w-2xl mx-auto">
<h2 class="text-2xl font-bold text-gray-800 mb-6">Merchant Registration</h2>
<div class="grid grid-cols-2 gap-6 mb-6">
<div>
<label class="block text-sm font-medium text-gray-700 mb-1">Business Name</label>
<input type="text" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500" />
</div>
<div>
<label class="block text-sm font-medium text-gray-700 mb-1">Business Type</label>
<select class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500">
<option>Education</option>
<option>Fitness & Gym</option>
<option>Car Services</option>
<option>Food & Beverage</option>
<option>Other</option>
</select>
</div>
<div>
<label class="block text-sm font-medium text-gray-700 mb-1">Business Email</label>
<input type="email" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500" />
</div>
<div>
<label class="block text-sm font-medium text-gray-700 mb-1">Business Phone</label>
<input type="tel" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500" />
</div>
</div>
<div class="grid grid-cols-2 gap-6 mb-8">
<div class="border border-gray-200 rounded-lg p-4 flex flex-col items-center justify-center">
<div class="w-20 h-20 bg-blue-50 rounded-full flex items-center justify-center mb-4">
<i class="fas fa-building text-blue-600 text-3xl"></i>
</div>
<h3 class="font-medium text-gray-800 mb-2">Business Credentials</h3>
<p class="text-sm text-gray-500 text-center mb-4">Upload your business license and registration documents</p>
<button class="px-4 py-2 bg-blue-100 text-blue-600 rounded-md font-medium text-sm cursor-pointer whitespace-nowrap !rounded-button">
<i class="fas fa-upload mr-2"></i>
Upload Business Documents
</button>
</div>
<div class="border border-gray-200 rounded-lg p-4 flex flex-col items-center justify-center">
<div class="w-20 h-20 bg-blue-50 rounded-full flex items-center justify-center mb-4">
<i class="fas fa-image text-blue-600 text-3xl"></i>
</div>
<h3 class="font-medium text-gray-800 mb-2">Business Profile</h3>
<p class="text-sm text-gray-500 text-center mb-4">Upload your business logo and storefront photos</p>
<button class="px-4 py-2 bg-blue-100 text-blue-600 rounded-md font-medium text-sm cursor-pointer whitespace-nowrap !rounded-button">
<i class="fas fa-upload mr-2"></i>
Upload Business Images
</button>
</div>
</div>
<div class="flex justify-center">
<button
id="completeRegistrationBtn"
@click="handleRegistrationComplete"
class="px-8 py-3 bg-blue-600 text-white font-medium rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 cursor-pointer whitespace-nowrap !rounded-button">
Complete Registration
</button>
<!-- Confirmation Dialog -->
<div v-if="showConfirmDialog" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
<div class="bg-white rounded-lg p-8 max-w-md w-full mx-4">
<h3 class="text-xl font-bold text-gray-900 mb-4">Confirm Registration</h3>
<div class="mb-6">
<div class="grid grid-cols-2 gap-4 mb-4">
<div>
<p class="text-sm text-gray-500">First Name</p>
<p class="font-medium">{{ registrationData.firstName || 'Not provided' }}</p>
</div>
<div>
<p class="text-sm text-gray-500">Last Name</p>
<p class="font-medium">{{ registrationData.lastName || 'Not provided' }}</p>
</div>
<div>
<p class="text-sm text-gray-500">Email</p>
<p class="font-medium">{{ registrationData.email || 'Not provided' }}</p>
</div>
<div>
<p class="text-sm text-gray-500">Phone</p>
<p class="font-medium">{{ registrationData.phone || 'Not provided' }}</p>
</div>
</div>
<div class="text-sm text-gray-500 mb-2">Verification Status</div>
<div class="flex items-center space-x-2 mb-1">
<i class="fas" :class="registrationData.biometricData ? 'fa-check text-green-500' : 'fa-times text-red-500'"></i>
<span>Biometric Data</span>
</div>
<div class="flex items-center space-x-2">
<i class="fas" :class="registrationData.documentsUploaded ? 'fa-check text-green-500' : 'fa-times text-red-500'"></i>
<span>Documents Uploaded</span>
</div>
</div>
<div class="flex justify-end space-x-4">
<button
@click="handleEdit"
class="px-4 py-2 text-gray-700 bg-gray-100 rounded-md hover:bg-gray-200 font-medium cursor-pointer whitespace-nowrap !rounded-button">
Edit
</button>
<button
@click="handleConfirm"
class="px-4 py-2 text-white bg-blue-600 rounded-md hover:bg-blue-700 font-medium cursor-pointer whitespace-nowrap !rounded-button">
Confirm
</button>
</div>
</div>
</div>
<!-- Success Message -->
<div v-if="showSuccessMessage" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
<div class="bg-white rounded-lg p-8 max-w-md w-full mx-4 text-center">
<div class="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
<i class="fas fa-check text-green-500 text-2xl"></i>
</div>
<h3 class="text-xl font-bold text-gray-900 mb-2">Registration Successful!</h3>
<p class="text-gray-600 mb-4">Please check your email to complete the verification process.</p>
<div class="animate-spin h-8 w-8 border-4 border-blue-600 border-t-transparent rounded-full mx-auto"></div>
<p class="text-sm text-gray-500 mt-4">Redirecting to dashboard...</p>
</div>
</div>
</div>
</div>
</div>
<!-- Contract Agreement Screen -->
<div v-if="activeTab === 'contract'" class="bg-white rounded-lg shadow-lg p-8 mb-8">
<h2 class="text-2xl font-bold text-gray-800 mb-8 text-center">Select Payment Model</h2>
<div class="grid grid-cols-2 gap-8 mb-12">
<div class="border border-gray-200 rounded-lg p-6 hover:border-blue-500 hover:shadow-md transition-all cursor-pointer relative">
<div class="absolute top-4 right-4">
<input type="radio" name="payment-model" class="w-5 h-5 text-blue-600" checked />
</div>
<div class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mb-4">
<i class="fas fa-hand-holding-usd text-blue-600 text-2xl"></i>
</div>
<h3 class="text-xl font-bold text-gray-800 mb-2">Pay After Use</h3>
<p class="text-gray-600 mb-4">Pay only after you've received the service, secured by smart contract.</p>
<ul class="space-y-2">
<li class="flex items-start">
<i class="fas fa-check text-green-500 mt-1 mr-2"></i>
<span class="text-sm text-gray-600">No upfront payment required</span>
</li>
<li class="flex items-start">
<i class="fas fa-check text-green-500 mt-1 mr-2"></i>
<span class="text-sm text-gray-600">Automatic payment release after service completion</span>
</li>
<li class="flex items-start">
<i class="fas fa-check text-green-500 mt-1 mr-2"></i>
<span class="text-sm text-gray-600">Protected by credit score system</span>
</li>
</ul>
</div>
<div class="border border-gray-200 rounded-lg p-6 hover:border-blue-500 hover:shadow-md transition-all cursor-pointer relative">
<div class="absolute top-4 right-4">
<input type="radio" name="payment-model" class="w-5 h-5 text-blue-600" />
</div>
<div class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mb-4">
<i class="fas fa-money-check-alt text-blue-600 text-2xl"></i>
</div>
<h3 class="text-xl font-bold text-gray-800 mb-2">Pay Before Use</h3>
<p class="text-gray-600 mb-4">Traditional prepayment with smart contract protection against defaults.</p>
<ul class="space-y-2">
<li class="flex items-start">
<i class="fas fa-check text-green-500 mt-1 mr-2"></i>
<span class="text-sm text-gray-600">Protected prepayment with escrow</span>
</li>
<li class="flex items-start">
<i class="fas fa-check text-green-500 mt-1 mr-2"></i>
<span class="text-sm text-gray-600">Automatic refund if service not delivered</span>
</li>
<li class="flex items-start">
<i class="fas fa-check text-green-500 mt-1 mr-2"></i>
<span class="text-sm text-gray-600">Potential discounts from merchants</span>
</li>
</ul>
</div>
</div>
<h3 class="text-xl font-bold text-gray-800 mb-6">Select Service Category</h3>
<div class="grid grid-cols-4 gap-6 mb-8">
<div v-for="(category, index) in serviceCategories" :key="index" class="border border-gray-200 rounded-lg p-4 hover:border-blue-500 hover:shadow-md transition-all cursor-pointer flex flex-col items-center">
<div class="w-16 h-16 rounded-full flex items-center justify-center mb-3 overflow-hidden">
<img :src="category.image" alt="Category image" class="w-full h-full object-cover" />
</div>
<h4 class="font-medium text-gray-800 mb-1">{{ category.name }}</h4>
<p class="text-xs text-gray-500 text-center">{{ category.description }}</p>
</div>
</div>
<div class="flex justify-center">
<a href="https://readdy.ai/home/f575dccc-a4be-4fc3-8140-3e96597a7875/d428787c-9de5-4bf4-a6ca-3c661d0050d8" data-readdy="true">
  <button
    class="px-8 py-3 bg-blue-600 text-white font-medium rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 cursor-pointer whitespace-nowrap !rounded-button">
    Construct Contract
  </button>
</a>
</div>
</div>
<!-- Daily Consumption Screen -->
<div v-if="activeTab === 'consumption'" class="bg-white rounded-lg shadow-lg p-8 mb-8">
<div class="flex justify-between items-center mb-8">
<div>
<h2 class="text-2xl font-bold text-gray-800">Active Contracts</h2>
<p class="text-gray-500">Manage your ongoing service contracts</p>
</div>
<div class="flex items-center space-x-4">
<div class="bg-blue-50 px-4 py-2 rounded-md">
<span class="text-sm text-gray-600">Balance:</span>
<span class="ml-1 font-bold text-gray-800">$2,450.00</span>
</div>
<div class="bg-green-50 px-4 py-2 rounded-md">
<span class="text-sm text-gray-600">Credit Score:</span>
<span class="ml-1 font-bold text-green-600">850</span>
<i class="fas fa-arrow-up text-green-600 ml-1 text-xs"></i>
</div>
</div>
</div>
<div class="grid grid-cols-2 gap-6 mb-8">
<div v-for="(contract, index) in activeContracts" :key="index" class="border border-gray-200 rounded-lg p-6 hover:shadow-md transition-all">
<div class="flex justify-between items-start mb-4">
<div class="flex items-center">
<div class="w-12 h-12 rounded-full overflow-hidden mr-4">
<img :src="contract.merchantImage" alt="Merchant logo" class="w-full h-full object-cover" />
</div>
<div>
<h3 class="font-bold text-gray-800">{{ contract.merchantName }}</h3>
<p class="text-sm text-gray-500">{{ contract.serviceType }}</p>
</div>
</div>
<div :class="[
'px-3 py-1 rounded-full text-xs font-medium',
contract.status === 'Active' ? 'bg-green-100 text-green-800' :
contract.status === 'Pending' ? 'bg-yellow-100 text-yellow-800' :
'bg-red-100 text-red-800'
]">
{{ contract.status }}
</div>
</div>
<div class="mb-4">
<div class="flex justify-between text-sm mb-1">
<span class="text-gray-600">Payment Progress</span>
<span class="font-medium text-gray-800">{{ contract.progress }}%</span>
</div>
<div class="w-full bg-gray-200 rounded-full h-2">
<div
class="bg-blue-600 h-2 rounded-full"
:style="{ width: `${contract.progress}%` }"
></div>
</div>
</div>
<div class="grid grid-cols-2 gap-4 mb-4">
<div>
<p class="text-xs text-gray-500">Total Amount</p>
<p class="font-bold text-gray-800">${{ contract.totalAmount.toFixed(2) }}</p>
</div>
<div>
<p class="text-xs text-gray-500">Remaining</p>
<p class="font-bold text-gray-800">${{ contract.remainingAmount.toFixed(2) }}</p>
</div>
<div>
<p class="text-xs text-gray-500">Next Payment</p>
<p class="font-medium text-gray-800">{{ contract.nextPaymentDate }}</p>
</div>
<div>
<p class="text-xs text-gray-500">Contract End</p>
<p class="font-medium text-gray-800">{{ contract.endDate }}</p>
</div>
</div>
<div class="flex space-x-3">
<button class="flex-1 px-4 py-2 bg-blue-600 text-white text-sm font-medium rounded-md hover:bg-blue-700 cursor-pointer whitespace-nowrap !rounded-button">
Make Payment
</button>
<button class="px-4 py-2 bg-gray-100 text-gray-700 text-sm font-medium rounded-md hover:bg-gray-200 cursor-pointer whitespace-nowrap !rounded-button">
Details
</button>
</div>
</div>
</div>
<h3 class="text-xl font-bold text-gray-800 mb-4">Recent Transactions</h3>
<div class="border border-gray-200 rounded-lg overflow-hidden mb-8">
<table class="min-w-full divide-y divide-gray-200">
<thead class="bg-gray-50">
<tr>
<th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Merchant</th>
<th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Date</th>
<th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Amount</th>
<th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
<th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Type</th>
</tr>
</thead>
<tbody class="bg-white divide-y divide-gray-200">
<tr v-for="(transaction, index) in transactions" :key="index" class="hover:bg-gray-50">
<td class="px-6 py-4 whitespace-nowrap">
<div class="flex items-center">
<div class="flex-shrink-0 h-8 w-8 rounded-full overflow-hidden">
<img :src="transaction.merchantImage" alt="Merchant logo" class="h-full w-full object-cover" />
</div>
<div class="ml-4">
<div class="text-sm font-medium text-gray-900">{{ transaction.merchantName }}</div>
<div class="text-xs text-gray-500">{{ transaction.serviceType }}</div>
</div>
</div>
</td>
<td class="px-6 py-4 whitespace-nowrap">
<div class="text-sm text-gray-900">{{ transaction.date }}</div>
</td>
<td class="px-6 py-4 whitespace-nowrap">
<div class="text-sm font-medium text-gray-900">${{ transaction.amount.toFixed(2) }}</div>
</td>
<td class="px-6 py-4 whitespace-nowrap">
<span :class="[
'px-2 py-1 inline-flex text-xs leading-5 font-semibold rounded-full',
transaction.status === 'Completed' ? 'bg-green-100 text-green-800' :
transaction.status === 'Pending' ? 'bg-yellow-100 text-yellow-800' :
'bg-red-100 text-red-800'
]">
{{ transaction.status }}
</span>
</td>
<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
{{ transaction.type }}
</td>
</tr>
</tbody>
</table>
</div>
<div class="bg-yellow-50 border border-yellow-200 rounded-lg p-4 mb-4">
<div class="flex items-start">
<div class="flex-shrink-0">
<i class="fas fa-exclamation-triangle text-yellow-400 mt-0.5"></i>
</div>
<div class="ml-3">
<h3 class="text-sm font-medium text-yellow-800">Payment Reminder</h3>
<div class="mt-2 text-sm text-yellow-700">
<p>You have a payment due in 3 days for FitLife Gym. Missing payments may affect your credit score.</p>
</div>
</div>
</div>
</div>
</div>
<!-- Contract Termination Screen -->
<div v-if="activeTab === 'termination'" class="bg-white rounded-lg shadow-lg p-8 mb-8">
<h2 class="text-2xl font-bold text-gray-800 mb-8 text-center">Contract Termination</h2>
<div class="max-w-3xl mx-auto">
<div class="border border-gray-200 rounded-lg p-6 mb-8">
<div class="flex items-center justify-center mb-6">
<div class="w-20 h-20 bg-red-100 rounded-full flex items-center justify-center">
<i class="fas fa-file-contract text-red-600 text-3xl"></i>
</div>
</div>
<h3 class="text-xl font-bold text-center text-gray-800 mb-2">Contract Status: Termination Requested</h3>
<p class="text-center text-gray-600 mb-6">You have requested to terminate your contract with EduTech Academy</p>
<div class="bg-gray-50 rounded-lg p-4 mb-6">
<h4 class="font-medium text-gray-800 mb-2">Termination Details</h4>
<div class="grid grid-cols-2 gap-4">
<div>
<p class="text-xs text-gray-500">Merchant</p>
<p class="font-medium text-gray-800">EduTech Academy</p>
</div>
<div>
<p class="text-xs text-gray-500">Service Type</p>
<p class="font-medium text-gray-800">Online Course Subscription</p>
</div>
<div>
<p class="text-xs text-gray-500">Termination Requested</p>
<p class="font-medium text-gray-800">April 22, 2025</p>
</div>
<div>
<p class="text-xs text-gray-500">Effective Date</p>
<p class="font-medium text-gray-800">May 1, 2025</p>
</div>
</div>
</div>
<div class="bg-gray-50 rounded-lg p-4 mb-6">
<h4 class="font-medium text-gray-800 mb-2">Financial Settlement</h4>
<div class="grid grid-cols-2 gap-4">
<div>
<p class="text-xs text-gray-500">Total Contract Value</p>
<p class="font-medium text-gray-800">$1,200.00</p>
</div>
<div>
<p class="text-xs text-gray-500">Amount Paid</p>
<p class="font-medium text-gray-800">$800.00</p>
</div>
<div>
<p class="text-xs text-gray-500">Refund Amount</p>
<p class="font-medium text-green-600">$200.00</p>
</div>
<div>
<p class="text-xs text-gray-500">Final Payment Due</p>
<p class="font-medium text-red-600">$0.00</p>
</div>
</div>
</div>
<div class="flex justify-center space-x-4">
<button class="px-6 py-2 bg-red-600 text-white font-medium rounded-md hover:bg-red-700 cursor-pointer whitespace-nowrap !rounded-button">
Confirm Termination
</button>
<button class="px-6 py-2 bg-gray-100 text-gray-700 font-medium rounded-md hover:bg-gray-200 cursor-pointer whitespace-nowrap !rounded-button">
Cancel Request
</button>
</div>
</div>
<div class="mb-8">
<h3 class="text-xl font-bold text-gray-800 mb-4">Termination Timeline</h3>
<div class="relative">
<div class="absolute left-4 top-0 h-full w-0.5 bg-gray-200"></div>
<div v-for="(event, index) in terminationTimeline" :key="index" class="relative pl-12 pb-8">
<div class="absolute left-0 top-1 w-8 h-8 rounded-full bg-blue-100 flex items-center justify-center z-10">
<i :class="['text-blue-600', event.icon]"></i>
</div>
<div>
<h4 class="text-sm font-medium text-gray-800">{{ event.title }}</h4>
<p class="text-xs text-gray-500 mb-1">{{ event.date }}</p>
<p class="text-sm text-gray-600">{{ event.description }}</p>
</div>
</div>
</div>
</div>
<div class="bg-blue-50 border border-blue-200 rounded-lg p-4">
<div class="flex">
<div class="flex-shrink-0">
<i class="fas fa-info-circle text-blue-500 mt-0.5"></i>
</div>
<div class="ml-3">
<h3 class="text-sm font-medium text-blue-800">Need Assistance?</h3>
<div class="mt-2 text-sm text-blue-700">
<p>If you have questions about your contract termination, please contact our support team at support@paobuliao.com or call 1-800-123-4567.</p>
</div>
<div class="mt-4">
<button class="px-4 py-2 bg-blue-100 text-blue-600 rounded-md text-sm font-medium cursor-pointer whitespace-nowrap !rounded-button">
Contact Support
</button>
</div>
</div>
</div>
</div>
</div>
</div>
</main>
<!-- Footer -->
<footer class="bg-gray-800 text-white py-12">
<div class="container mx-auto px-6">
<div class="grid grid-cols-4 gap-8 mb-8">
<div>
<h3 class="text-lg font-bold mb-4">Paobuliao</h3>
<p class="text-gray-400 text-sm">A decentralized application based on smart contracts to protect prepaid services and prevent defaults.</p>
</div>
<div>
<h3 class="text-lg font-bold mb-4">Quick Links</h3>
<ul class="space-y-2">
<li><a href="#" class="text-gray-400 hover:text-white text-sm">How It Works</a></li>
<li><a href="#" class="text-gray-400 hover:text-white text-sm">For Merchants</a></li>
<li><a href="#" class="text-gray-400 hover:text-white text-sm">For Users</a></li>
<li><a href="#" class="text-gray-400 hover:text-white text-sm">Smart Contracts</a></li>
</ul>
</div>
<div>
<h3 class="text-lg font-bold mb-4">Support</h3>
<ul class="space-y-2">
<li><a href="#" class="text-gray-400 hover:text-white text-sm">Help Center</a></li>
<li><a href="#" class="text-gray-400 hover:text-white text-sm">Contact Us</a></li>
<li><a href="#" class="text-gray-400 hover:text-white text-sm">FAQ</a></li>
<li><a href="#" class="text-gray-400 hover:text-white text-sm">Privacy Policy</a></li>
</ul>
</div>
<div>
<h3 class="text-lg font-bold mb-4">Connect With Us</h3>
<div class="flex space-x-4 mb-4">
<a href="#" class="text-gray-400 hover:text-white">
<i class="fab fa-twitter text-xl"></i>
</a>
<a href="#" class="text-gray-400 hover:text-white">
<i class="fab fa-facebook text-xl"></i>
</a>
<a href="#" class="text-gray-400 hover:text-white">
<i class="fab fa-linkedin text-xl"></i>
</a>
<a href="#" class="text-gray-400 hover:text-white">
<i class="fab fa-github text-xl"></i>
</a>
</div>
<p class="text-gray-400 text-sm">Subscribe to our newsletter</p>
<div class="flex mt-2">
<input type="email" placeholder="Your email" class="px-4 py-2 text-sm text-gray-800 rounded-l-md border-none focus:outline-none focus:ring-0" />
<button class="bg-blue-600 px-4 py-2 rounded-r-md text-sm font-medium cursor-pointer whitespace-nowrap !rounded-button">Subscribe</button>
</div>
</div>
</div>
<div class="pt-8 border-t border-gray-700 flex justify-between items-center">
<p class="text-gray-400 text-sm">© 2025 Paobuliao. All rights reserved.</p>
<div class="flex space-x-4">
<i class="fab fa-cc-visa text-gray-400 text-2xl"></i>
<i class="fab fa-cc-mastercard text-gray-400 text-2xl"></i>
<i class="fab fa-cc-paypal text-gray-400 text-2xl"></i>
<i class="fab fa-bitcoin text-gray-400 text-2xl"></i>
<i class="fab fa-ethereum text-gray-400 text-2xl"></i>
</div>
</div>
</div>
</footer>
</div>
</template>
<script lang="ts" setup>
import { ref, onMounted } from 'vue';
// Registration form data
const registrationData = ref({
firstName: '',
lastName: '',
email: '',
phone: '',
biometricData: false,
documentsUploaded: false
});
// Dialog states
const showConfirmDialog = ref(false);
const showSuccessMessage = ref(false);
// Handle registration completion
const handleRegistrationComplete = () => {
showConfirmDialog.value = true;
};
// Handle confirmation
const handleConfirm = () => {
showConfirmDialog.value = false;
showSuccessMessage.value = true;
// Simulate email sending
console.log('Sending verification email to:', registrationData.value.email);
// Change tab after delay
setTimeout(() => {
showSuccessMessage.value = false;
activeTab.value = 'contract';
}, 3000);
};
// Handle edit
const handleEdit = () => {
showConfirmDialog.value = false;
};
// Navigation tabs
const tabs = [
{ id: 'registration', name: 'Registration', icon: 'fas fa-user-plus' },
{ id: 'contract', name: 'Contract Agreement', icon: 'fas fa-file-contract' },
{ id: 'consumption', name: 'Daily Consumption', icon: 'fas fa-chart-line' },
{ id: 'termination', name: 'Contract Termination', icon: 'fas fa-times-circle' }
];
const activeTab = ref('registration');
// Navigation menu
const navigationMenu = ref([
{ id: 'contract', name: 'Contract Agreement', icon: 'fas fa-file-contract', active: false },
{ id: 'consumption', name: 'Daily Consumption', icon: 'fas fa-chart-line', active: false },
{ id: 'termination', name: 'Contract Termination', icon: 'fas fa-times-circle', active: false }
]);
// Handle tab change
const changeTab = (tabId: string) => {
activeTab.value = tabId;
};
const registrationType = ref('user');
// Service categories
const serviceCategories = [
{
name: 'Education',
description: 'Schools, courses, tutoring services',
image: 'https://readdy.ai/api/search-image?query=modern%20education%20icon%20with%20books%20and%20graduation%20cap%20on%20a%20clean%20blue%20gradient%20background%2C%20minimalist%20design%2C%20professional%20looking%2C%20high%20quality%20detailed%20illustration&width=100&height=100&seq=1&orientation=squarish'
},
{
name: 'Fitness & Gym',
description: 'Gym memberships, fitness classes',
image: 'https://readdy.ai/api/search-image?query=modern%20fitness%20and%20gym%20icon%20with%20dumbbells%20and%20exercise%20equipment%20on%20a%20clean%20blue%20gradient%20background%2C%20minimalist%20design%2C%20professional%20looking%2C%20high%20quality%20detailed%20illustration&width=100&height=100&seq=2&orientation=squarish'
},
{
name: 'Car Services',
description: 'Car wash, maintenance, repair',
image: 'https://readdy.ai/api/search-image?query=modern%20car%20service%20icon%20with%20car%20and%20tools%20on%20a%20clean%20blue%20gradient%20background%2C%20minimalist%20design%2C%20professional%20looking%2C%20high%20quality%20detailed%20illustration&width=100&height=100&seq=3&orientation=squarish'
},
{
name: 'Food & Beverage',
description: 'Restaurants, cafes, meal plans',
image: 'https://readdy.ai/api/search-image?query=modern%20food%20and%20beverage%20icon%20with%20plate%20and%20utensils%20on%20a%20clean%20blue%20gradient%20background%2C%20minimalist%20design%2C%20professional%20looking%2C%20high%20quality%20detailed%20illustration&width=100&height=100&seq=4&orientation=squarish'
},
{
name: 'Beauty & Spa',
description: 'Salons, spas, beauty treatments',
image: 'https://readdy.ai/api/search-image?query=modern%20beauty%20and%20spa%20icon%20with%20lotus%20flower%20and%20massage%20stones%20on%20a%20clean%20blue%20gradient%20background%2C%20minimalist%20design%2C%20professional%20looking%2C%20high%20quality%20detailed%20illustration&width=100&height=100&seq=5&orientation=squarish'
},
{
name: 'Housing',
description: 'Rent, utilities, maintenance',
image: 'https://readdy.ai/api/search-image?query=modern%20housing%20icon%20with%20house%20and%20key%20on%20a%20clean%20blue%20gradient%20background%2C%20minimalist%20design%2C%20professional%20looking%2C%20high%20quality%20detailed%20illustration&width=100&height=100&seq=6&orientation=squarish'
},
{
name: 'Entertainment',
description: 'Streaming, events, subscriptions',
image: 'https://readdy.ai/api/search-image?query=modern%20entertainment%20icon%20with%20movie%20ticket%20and%20popcorn%20on%20a%20clean%20blue%20gradient%20background%2C%20minimalist%20design%2C%20professional%20looking%2C%20high%20quality%20detailed%20illustration&width=100&height=100&seq=7&orientation=squarish'
},
{
name: 'Other Services',
description: 'Custom service agreements',
image: 'https://readdy.ai/api/search-image?query=modern%20miscellaneous%20services%20icon%20with%20gear%20and%20tools%20on%20a%20clean%20blue%20gradient%20background%2C%20minimalist%20design%2C%20professional%20looking%2C%20high%20quality%20detailed%20illustration&width=100&height=100&seq=8&orientation=squarish'
}
];
// Active contracts
const activeContracts = [
{
merchantName: 'EduTech Academy',
merchantImage: 'https://readdy.ai/api/search-image?query=modern%20education%20company%20logo%20with%20blue%20and%20white%20colors%2C%20professional%2C%20clean%20design%20on%20white%20background%2C%20minimalist%2C%20high%20quality&width=100&height=100&seq=9&orientation=squarish',
serviceType: 'Online Course Subscription',
status: 'Active',
progress: 65,
totalAmount: 1200,
remainingAmount: 420,
nextPaymentDate: 'May 1, 2025',
endDate: 'Oct 31, 2025'
},
{
merchantName: 'FitLife Gym',
merchantImage: 'https://readdy.ai/api/search-image?query=modern%20fitness%20gym%20logo%20with%20blue%20and%20white%20colors%2C%20professional%2C%20clean%20design%20on%20white%20background%2C%20minimalist%2C%20high%20quality&width=100&height=100&seq=10&orientation=squarish',
serviceType: 'Annual Membership',
status: 'Active',
progress: 30,
totalAmount: 840,
remainingAmount: 588,
nextPaymentDate: 'Apr 27, 2025',
endDate: 'Feb 28, 2026'
}
];
// Transactions
const transactions = [
{
merchantName: 'EduTech Academy',
merchantImage: 'https://readdy.ai/api/search-image?query=modern%20education%20company%20logo%20with%20blue%20and%20white%20colors%2C%20professional%2C%20clean%20design%20on%20white%20background%2C%20minimalist%2C%20high%20quality&width=100&height=100&seq=9&orientation=squarish',
serviceType: 'Online Course',
date: 'Apr 20, 2025',
amount: 120,
status: 'Completed',
type: 'Automatic Payment'
},
{
merchantName: 'FitLife Gym',
merchantImage: 'https://readdy.ai/api/search-image?query=modern%20fitness%20gym%20logo%20with%20blue%20and%20white%20colors%2C%20professional%2C%20clean%20design%20on%20white%20background%2C%20minimalist%2C%20high%20quality&width=100&height=100&seq=10&orientation=squarish',
serviceType: 'Membership',
date: 'Apr 15, 2025',
amount: 70,
status: 'Completed',
type: 'Automatic Payment'
},
{
merchantName: 'SparkleWash',
merchantImage: 'https://readdy.ai/api/search-image?query=modern%20car%20wash%20logo%20with%20blue%20and%20white%20colors%2C%20professional%2C%20clean%20design%20on%20white%20background%2C%20minimalist%2C%20high%20quality&width=100&height=100&seq=11&orientation=squarish',
serviceType: 'Car Wash',
date: 'Apr 10, 2025',
amount: 35,
status: 'Completed',
type: 'One-time Payment'
},
{
merchantName: 'EduTech Academy',
merchantImage: 'https://readdy.ai/api/search-image?query=modern%20education%20company%20logo%20with%20blue%20and%20white%20colors%2C%20professional%2C%20clean%20design%20on%20white%20background%2C%20minimalist%2C%20high%20quality&width=100&height=100&seq=9&orientation=squarish',
serviceType: 'Online Course',
date: 'Apr 27, 2025',
amount: 120,
status: 'Pending',
type: 'Scheduled Payment'
}
];
// Termination timeline
const terminationTimeline = [
{
title: 'Termination Request Submitted',
date: 'April 22, 2025',
description: 'You submitted a request to terminate your contract with EduTech Academy.',
icon: 'fas fa-file-alt'
},
{
title: 'Merchant Notified',
date: 'April 22, 2025',
description: 'EduTech Academy has been notified of your termination request.',
icon: 'fas fa-bell'
},
{
title: 'Refund Calculation',
date: 'April 23, 2025',
description: 'Smart contract calculated the refund amount based on usage and terms.',
icon: 'fas fa-calculator'
},
{
title: 'Pending Confirmation',
date: 'Current Stage',
description: 'Waiting for your confirmation to process the termination and refund.',
icon: 'fas fa-clock'
},
{
title: 'Contract Termination',
date: 'Pending',
description: 'Once confirmed, the contract will be terminated and refund processed.',
icon: 'fas fa-check-circle'
}
];
</script>
<style scoped>
/* Custom styles */
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
-webkit-appearance: none;
margin: 0;
}
input[type="number"] {
-moz-appearance: textfield;
}
/* Dialog animation */
.fixed {
animation: fadeIn 0.3s ease-out;
}
@keyframes fadeIn {
from {
opacity: 0;
transform: translateY(-20px);
}
to {
opacity: 1;
transform: translateY(0);
}
}
</style>
