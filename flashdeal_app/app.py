// App.js
import React from 'react';
import { SafeAreaView, StyleSheet, Text, View, FlatList, TouchableOpacity } from 'react-native';

// بيانات تجريبية (يمكنك ربطها بـ API لاحقًا)
const deals = [
  { id: '1', title: 'خصم 50% على القهوة', price: '5 TND', rating: 4.5 },
  { id: '2', title: 'عرض خاص على البيتزا', price: '12 TND', rating: 4.0 },
  { id: '3', title: 'تخفيض على الكتب', price: '20 TND', rating: 5.0 },
];

// مكوّن لعرض بطاقة العرض
const DealCard = ({ title, price, rating }) => (
  <View style={styles.card}>
    <Text style={styles.title}>{title}</Text>
    <Text style={styles.price}>{price}</Text>
    <Text style={styles.rating}>⭐ {rating}</Text>
    <TouchableOpacity style={styles.button}>
      <Text style={styles.buttonText}>اشترِ الآن</Text>
    </TouchableOpacity>
  </View>
);

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.header}>FlashDeal Star ✨</Text>
      <FlatList
        data={deals}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <DealCard title={item.title} price={item.price} rating={item.rating} />
        )}
      />
    </SafeAreaView>
  );
}

// الأنماط
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fefefe',
    padding: 16,
  },
  header: {
    fontSize: 26,
    fontWeight: 'bold',
    textAlign: 'center',
    marginVertical: 12,
    color: '#333',
  },
  card: {
    backgroundColor: '#fff',
    padding: 16,
    marginVertical: 8,
    borderRadius: 12,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowRadius: 6,
    elevation: 3,
  },
  title: {
    fontSize: 18,
    fontWeight: '600',
    marginBottom: 6,
  },
  price: {
    fontSize: 16,
    color: '#007BFF',
    marginBottom: 6,
  },
  rating: {
    fontSize: 14,
    color: '#888',
    marginBottom: 10,
  },
  button: {
    backgroundColor: '#FF5722',
    paddingVertical: 10,
    borderRadius: 8,
  },
  buttonText: {
    color: '#fff',
    textAlign: 'center',
    fontWeight: 'bold',
  },
});
