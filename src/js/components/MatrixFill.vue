<script setup>
import {onBeforeMount,ref} from "vue";

const props = defineProps({
    ren: Number,
    col: Number,
    matrix: Array
})

const emit = defineEmits(['update:matrix'])

const matrix = ref([]);

onBeforeMount(e => {
    // nemoas la matriz en memoria
    for(let i = 0; i < props.ren; i++){
        let row = []
        for(let j = 0; j < props.col; j++){
            row.push(0)
        }
        matrix.value.push(row);
    }
})

function updateMatrix(){
    emit('update:matrix',matrix.value)
}

</script>

<template>
    <div>
        <h5>Llenar matriz</h5>
        <table class="u-full-width">
            <tr v-for="r in ren">
                <td v-for="c in col">
                    <span>{{ r }}, {{ c }}</span>
                    <input type="number"
                           @input="updateMatrix"
                           v-model.number="matrix[r - 1][c - 1]"
                           :name="'c_' + (r + '') + '_'+ (c +1)"
                           :id="'c_' + (r + '') + '_'+ (c +1)"
                           style="display: inline-block"
                           class="u-full-width">
                </td>
            </tr>
        </table>
    </div>
</template>

<script>
export default {
    name: "MatrixFill"
}
</script>

<style scoped>

</style>