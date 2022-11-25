function a() {
  for (const i = 5; i < 9; i++) {
    try {
      break;
    } catch (e) {
      if (false) {
        return;
        break;
      }
    } finally {
      while (false) {
        continue;
      }
    }
  }
}
