def calculate_dui_program_cost():
  print("=== DUI Program 3-Month Transfer-In Calculator ===")
  print("Type 'r' to return to the previous question.\n")

  steps = [
      "Enter client's name: ",
      "Number of education classes (1 hr, $17 each): ",
      "Number of group classes (2 hrs, $54 each): ",
      "Number of face-to-face interviews ($25 each): ",
      "Is the client transferring from Ventura County? (yes/no): "
  ]

  responses = [""] * len(steps)
  step = 0

  while step < len(steps):
      response = input(steps[step])

      # Go back to previous step
      if response.lower() == "r":
          if step > 0:
              step -= 1
          else:
              print("You're at the first step. Cannot go back.")
          continue

      # Validation
      if step == 0:
          responses[step] = response
          step += 1
      elif step in [1, 2, 3]:  # numeric steps
          if response.isdigit():
              responses[step] = int(response)
              step += 1
          else:
              print("Please enter a valid number or 'r' to return.")
      elif step == 4:
          if response.lower() in ["yes", "no"]:
              responses[step] = response.lower()
              step += 1
          else:
              print("Please type 'yes', 'no', or 'r' to return.")

  # Assign inputs
  name = responses[0]
  num_education = responses[1]
  num_group = responses[2]
  num_face_to_face = responses[3]
  from_ventura = responses[4]

  # Fixed costs
  transfer_fee = 75
  education_cost = 17
  group_cost = 54
  face_to_face_cost = 25
  ventura_fee = 50 if from_ventura == "yes" else 0

  # Calculations
  total_education = num_education * education_cost
  total_group = num_group * group_cost
  total_face_to_face = num_face_to_face * face_to_face_cost
  total = total_education + total_group + total_face_to_face + transfer_fee + ventura_fee

  # Output
  print("\n=== Program Summary ===")
  print(f"Client Name: {name}")
  print(f"Education Classes: {num_education} x ${education_cost} = ${total_education}")
  print(f"Group Classes: {num_group} x ${group_cost} = ${total_group}")
  print(f"Face-to-Face Interviews: {num_face_to_face} x ${face_to_face_cost} = ${total_face_to_face}")
  print(f"Transfer Fee: ${transfer_fee}")
  if ventura_fee:
      print(f"Ventura County Fee: ${ventura_fee}")
  print(f"Total Program Cost: ${total}")

# Run the calculator
calculate_dui_program_cost()
