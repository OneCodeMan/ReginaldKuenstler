import SwiftUI

struct PaletteColourSelectItem: Identifiable {
    let id = UUID()
    var paletteColour: PaletteColour
    var isSelected: Bool
}

struct PaletteCreationView: View {
    @ObservedObject var viewModel: CreateUserPaletteViewModel = CreateUserPaletteViewModel()
    
    // MARK: Search logic
    @State private var searchText: String = ""
    
    // Grid layout with 3 columns
    let columns = Array(repeating: GridItem(.flexible()), count: 3)
    
    var body: some View {
        NavigationStack {
            VStack {
                List {
                    ForEach(viewModel.groupedColourSelectItems.keys.sorted(), id: \.self) { groupName in
                        GroupSectionView(groupName: groupName, colourItems: viewModel.groupedColourSelectItems[groupName] ?? [], viewModel: viewModel)
                    }
                }
                .searchable(text: $searchText)
                .onChange(of: searchText) { search in
                    if !search.isEmpty {
                        viewModel.filterPaletteColours(term: search)
                    } else {
                        viewModel.resetFilteredPaletteColours()
                    }
                }
                
                // Display selected colors
                SelectedColoursView(viewModel: viewModel)
                    .padding()
            }
            .navigationTitle("Create Palette")
            .onAppear {
                viewModel.fetchUserPalettes()
            }
        }
    }
}

struct GroupSectionView: View {
    var groupName: String
    var colourItems: [PaletteColourSelectItem]
    @ObservedObject var viewModel: CreateUserPaletteViewModel  // Pass viewModel here
    
    var body: some View {
        if !colourItems.isEmpty {
            VStack(alignment: .leading) {
                Text(groupName)
                    .font(.largeTitle)
                    .bold()
                    .padding([.top, .leading], 8)
                
                // Colour list
                ColourGridView(colourItems: colourItems, viewModel: viewModel)  // Pass viewModel to ColourGridView
            }
            .listRowSeparator(.hidden)
        }
    }
}

struct ColourGridView: View {
    var colourItems: [PaletteColourSelectItem]
    @ObservedObject var viewModel: CreateUserPaletteViewModel
    
    var body: some View {
        LazyVGrid(columns: Array(repeating: GridItem(.flexible()), count: 3)) {
            ForEach(colourItems) { cI in
                if let index = viewModel.filteredPaletteColourSelectItems.firstIndex(where: { $0.id == cI.id }) {
                    PaletteListItemView(paletteColourItem: $viewModel.filteredPaletteColourSelectItems[index])
                        .onTapGesture {
                            toggleColourSelection(for: cI)
                        }
                }
            }
            // end of foreach(colourItems)
        }
        .listRowSeparator(.hidden)
        .padding()
    }
    
    private func toggleColourSelection(for item: PaletteColourSelectItem) {
        // Update selection state
        if let index = viewModel.filteredPaletteColourSelectItems.firstIndex(where: { $0.id == item.id }) {
            if !viewModel.filteredPaletteColourSelectItems[index].paletteColour.isUserOwned {
                viewModel.filteredPaletteColourSelectItems[index].isSelected.toggle()
                print("Toggled selection for color: \(item.paletteColour.uiColour)")
            } else {
                print("user owned not toggling select")
            }
            
        }
    }
}

struct SelectedColoursView: View {
    @ObservedObject var viewModel: CreateUserPaletteViewModel
    
    // MARK: Dismiss
    @Environment(\.dismiss) var dismiss
    
    var body: some View {
        VStack(alignment: .center) {
            Text("Selected Colours:")
            HStack {
                ForEach(viewModel.filteredPaletteColourSelectItems.filter { $0.isSelected }) { pc in
                    Circle()
                        .stroke(.gray, lineWidth: 2)
                        .fill(Color(pc.paletteColour.uiColour))
                        .frame(height: 20)
                }
            }
            .padding()
            
            Button(action: {
                viewModel.saveSelectedToUserDefaults()
                dismiss() // Ensure this function is available
            }) {
                Text("Save Selected Colours")
                    .padding()
                    .background(viewModel.filteredPaletteColourSelectItems.filter { $0.isSelected }.isEmpty ? Color.gray : Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(8)
            }
            .disabled(viewModel.filteredPaletteColourSelectItems.filter { $0.isSelected }.isEmpty)
        }
    }
}
