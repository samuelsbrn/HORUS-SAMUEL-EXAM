<template>
  <table border="1" width="100%" cellspacing="0" cellpadding="10" style="border-collapse: collapse;">
    <thead style="background-color: #eee;">
      <tr>
        <th>ID</th>
        <th>Username</th>
        <th>Nama Lengkap</th>
        <th>Email</th>
        <th>Aksi</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="user in users" :key="user.id">
        <td>{{ user.id }}</td>
        <td>{{ user.username }}</td>
        <td>{{ user.nama }}</td>
        <td>{{ user.email }}</td>
        <td>
          <button class="btn" @click="$emit('edit', user)">[U] Update</button>
          <button class="btn btn-danger" @click="$emit('delete', user.id)">[H] Hapus</button>
        </td>
      </tr>
      <tr v-if="users.length === 0">
        <td colspan="5" style="text-align: center;">Tidak ada data pengguna.</td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';
defineProps({ users: Array });
defineEmits(['edit', 'delete']);
</script>