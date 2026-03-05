// screens/OnboardingScreen.js
import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet, Image } from 'react-native';
import i18n from '../i18n'; // ملفات ترجمة منفصلة ar.json, fr.json, en.json

export default function OnboardingScreen({ navigation }) {
  return (
    <View style={styles.container} accessible={true}>
      <Image 
        source={require('../assets/logo.png')} 
        style={styles.logo} 
        accessibilityLabel={i18n.t('app_logo')}
      />
      <Text style={styles.title}>{i18n.t('welcome')}</Text>
      <Text style={styles.subtitle}>{i18n.t('tagline')}</Text>

      <TouchableOpacity 
        style={styles.button} 
        onPress={() => navigation.navigate('Home')}
        accessibilityLabel={i18n.t('get_started')}
      >
        <Text style={styles.buttonText}>{i18n.t('get_started')}</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { 
    flex:1, 
    justifyContent:'center', 
    alignItems:'center', 
    backgroundColor:'#f9f9f9',
    padding:20 
  },
  logo: { width:120, height:120, marginBottom:20 },
  title: { fontSize:24, fontWeight:'bold', color:'#222', marginBottom:10 },
  subtitle: { fontSize:16, color:'#555', marginBottom:30, textAlign:'center', paddingHorizontal:20 },
  button: { backgroundColor:'#007AFF', paddingVertical:14, paddingHorizontal:40, borderRadius:10 },
  buttonText: { color:'#fff', fontSize:16, fontWeight:'600' }
});
