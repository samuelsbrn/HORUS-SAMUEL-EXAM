<template>
  <div class="search-bar" style="margin-bottom: 20px;">
    <input 
      type="text" 
      v-model="searchQuery" 
      placeholder="Cari Pengguna (Nama/Username)..." 
      style="padding: 8px; width: 300px; margin-right: 10px;"
      @input="onSearch"
    />
  </div>
</template>

<script setup>
import { ref, defineEmits } from 'vue';
const searchQuery = ref('');
const emit = defineEmits(['search']);

const onSearch = () => {
  emit('search', searchQuery.value);
};
</script>